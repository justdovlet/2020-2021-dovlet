---
# Front matter
lang: ru-RU
title: "Отчет по лабораторной работе №1"
subtitle: "НФИбд-02-18"
author: "Оразклычев Довлет"

# Formatting
toc-title: "Содержание"
toc: true # Table of contents
toc_depth: 2
lof: true # List of figures
lot: true # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4paper
documentclass: scrreprt
polyglossia-lang: russian
polyglossia-otherlangs: english
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase
indent: true
pdf-engine: lualatex
header-includes:
  - \linepenalty=10 # the penalty added to the badness of each line within a paragraph (no associated penalty node) Increasing the value makes tex try to have fewer lines in the paragraph.
  - \interlinepenalty=0 # value of the penalty (node) added after each line of a paragraph.
  - \hyphenpenalty=50 # the penalty for line breaking at an automatically inserted hyphen
  - \exhyphenpenalty=50 # the penalty for line breaking at an explicit hyphen
  - \binoppenalty=700 # the penalty for breaking a line at a binary operator
  - \relpenalty=500 # the penalty for breaking a line at a relation
  - \clubpenalty=150 # extra penalty for breaking after first line of a paragraph
  - \widowpenalty=150 # extra penalty for breaking before last line of a paragraph
  - \displaywidowpenalty=50 # extra penalty for breaking before last line before a display math
  - \brokenpenalty=100 # extra penalty for page breaking after a hyphenated line
  - \predisplaypenalty=10000 # penalty for breaking before a display
  - \postdisplaypenalty=0 # penalty for breaking after a display
  - \floatingpenalty = 20000 # penalty for splitting an insertion (can only be split footnote in standard LaTeX)
  - \raggedbottom # or \flushbottom
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы

Познакомиться с основными возможностями разметки Markdown и системы контроля версии Git

# Задание

Создать репозиторий на сайте github.com. Сделать первый коммит и пуш. Изменить код в текстовом файле. Сделать повторнйы коммит и пуш для того, чтобы увидеть разницу версии.

Создать отчет используя разметку Markdown в форматах pdf и docx.

Сделать презентацию работы используя Markdown.


# Выполнение лабораторной работы

Git 

Создаем репозиторий на сайте github.com (рис. -@fig:001)

![Новый репозиторий](image/01.png){ #fig:001 width=70% }

Создаем новую папку, добавляем файлы для публикации и делаем первый коммит и пуш (рис. -@fig:002)

![Новый репозиторий](image/02.png){ #fig:002 width=70% }

Изменяем несколько строк в текстовом файле и делаем снова коммит и пуш (рис. -@fig:003)

![Новый репозиторий](image/03.png){ #fig:003 width=70% }

Открываем репозиторий на сайте github.com и смотрим изменения версий текстового файла (рис. -@fig:004)

![Новый репозиторий](image/04.png){ #fig:004 width=70% }


Markdown 

Скачиваем шаллоны для Markdown и разархивируем его в папку для лабораторной работы (рис. -@fig:005)

![Новый репозиторий](image/05.png){ #fig:005 width=70% }

Редактируем шаблон для Markdown для создания отчета (рис. -@fig:006)

![Новый репозиторий](image/06.png){ #fig:006 width=70% }

Запускаем команду make дял преобразования шаблона в документ в форматах pdf и docx (рис. -@fig:007)

![Новый репозиторий](image/07.png){ #fig:007 width=70% }



# Выводы

Познакомились с основными функциями разметки Markdown и системы контроля версии Git
