# Модуль анимации

За обработку анимации отвечает отдельный модуль [animation](../../drone/modules/animation.py). При загрузке анимации на коптер модуль производит разделение последовательности кадров анимации на 5 ключевых этапов:

1. Коптер неподвижен в начале анимации - `static_begin`
2. Коптер взлетает - `takeoff`
3. Коптер следует по маршруту анимации - `route`
4. Коптер выполняет посадку - `land`
5. Коптер неподвижен до завершения файла анимации - `static_end`

Кадр анимации - это набор данных, необходимых для позиционирования коптера и определения цвета его подсветки. В текущей версии ПО кадр анимации представлен последовательностью чисел `x y z yaw r g b` в строке `.csv` файла с анимацией, где:

* `x`, `y`, `z` - координаты коптера в текущем кадре в метрах
* `yaw` - рыскание коптера в радианах
* `r`, `g`, `b` - компоненты цвета подсветки коптера, целые числа от 0 до 255

После разделения анимации на ключевые этапы модуль формирует выходную последовательность кадров, определяющих положение коптера и цвет его подсветки, а также последовательность действий при полёте к первой точке анимации.

Настройка модуля производится в разделе [ANIMATION](client.md#раздел-animation).

Первичный отбор кадров производится с помощью набора флагов [[OUTPUT]], устанавливающих, какие последовательности кадров из 5 ключевых этапов будут использованы в полёте, а какие - нет.

Ключевым параметром, определяющим логику воспроизведения анимации является параметр `start_action`, определяющий первое действие при запуске воспроизведения анимации. Доступные варианты его значений:

* `auto` - автоматический выбор действия между `takeoff` (взлёт) или `fly` (мгновенный полёт по точкам) на основе текущего уровня высоты коптера. Если (`z` в начальной точке анимации) > (уровень взлета `takeoff_level`), то значение устанавливается в `takeoff`, иначе значение устанавливается в `fly`.
* `fly` - выполнение *логики полёта по точкам*
* `takeoff` - выполнение *логики взлёта к первой точке*.

Если в файле анимации коптер взлетает с земли, при старте анимации будет применена **логика полёта по точкам (fly)**: коптер с выключенными моторами воспроизводит цвет из анимации, пока неподвижен, включает двигатели перед моментом взлёта, затем через время `arming_time` начинает следовать точкам, указанным в анимации.

Если в файле анимации коптер начинает полёт в воздухе, при старте анимации будет применена **логики взлёта к первой точке (takeoff)**: коптер с выключенными моторами воспроизводит цвет из анимации, пока неподвижен, включает двигатели перед моментом взлёта, затем взлетает на высоту `takeoff_height` за время `takeoff_time`, затем перемещается к первой точке за время `reach_first_point_time`, и затем начинает следовать точкам, указанным в анимации.

Если параметр `start_action` установлен в `takeoff`, а флаг `takeoff` в разделе [[OUTPUT]] установлен в значение `True`, то последовательность кадров со взлётом коптера по точкам заменяется на 2 последовательных действия:

* взлёт относительно текущей позиции на высоту `takeoff_height` за время `takeoff_time`
* полёт по прямой до начальной точки последовательности кадров маршрута коптера (`route`) за время `reach_first_point_time`

## Подготовка и загрузка анимации

Создайте анимацию объектов в [Blender](https://www.blender.org) или воспользуйтесь [примерами](../../examples/animations).

Коптер можно изобразить любым трёхмерным объектом (например кубом или шаром), а цвет подсветки ленты будет извлекаться при экспорте из свойства цвета объекта. При создании анимации учитывайте следующие факты и рекомендации:

* Для удобной конвертации и загрузки анимации на коптеры, объекты, соответствующие коптерам, должны иметь имена, соответствующие именам этих коптеров.
* Условная единица расстояния в Blender конвертируется в метры.
* Задержка между кадрами по-умолчанию в [настройках коптера](../../drone/config/spec/configspec_client.ini) равна 0.1 секунды (параметр `frame_delay` в разделе ANIMATION), будьте внимательны при настройке частоты кадров в анимации Blender.
* Следите за скоростями коптеров, чтобы они были не слишком большими (для помещения - не более 3 м/с, для улицы - не более 5 м/с): аддон выдаст предупреждение, но всё равно сконвертирует анимацию.

Сконвертируйте анимацию с помощью [аддона для Blender](blender-addon.md).

Если в анимации несколько объектов и их имена соответствуют именам коптеров, загрузите папку с анимацией на выделенные в таблице коптеры с помощью команды `Send -> Animations` на [сервере](server.md#раздел-selected-drones).

Также любой файл анимации можно загрузить отдельно на все выделенные в таблице коптеры с помощью команды `Send -> Animation`.

## Анализ анимации

Если вам нужна информация о том, по каким точкам полетит коптер в результате загрузки анимации по текущим параметрам клиента, возпользуйтесь утилитой [animation_info](../../tools/animation_info.py).

```cmd
usage: python animation_info.py [-h] [--config] [animation]

Get animation info

positional arguments:
  animation   Path to animation. Default is
              ../examples/animations/basic/basic.csv.

optional arguments:
  -h, --help  show this help message and exit
  --config    Set this option to print config info.
```

Данная утилита выводит полную информацию о настройках анимации и конфигурации клиента (опционально), а также выводит оба возможных варианта воспроизведения анимации, что позволяет проанализировать действия коптеров перед реальным полётом.