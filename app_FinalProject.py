import pandas as pd
import streamlit as st
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

image = Image.open('images.jpg')

data = pd.read_csv("data.csv")
data_Ins = pd.read_csv("data_Ins.csv")
data_Irs = pd.read_csv("data_Irs.csv")
data_RS = pd.read_csv("data_RS.csv")
data_2005_2021 = pd.read_csv("data_2005_2021.csv")
MF_DPI = pd.read_csv("MF_DPI.csv")
MF_Ed = pd.read_csv("MF_Ed.csv")
MF_Str = pd.read_csv("MF_Str.csv")

def main():
    page = st.sidebar.selectbox("Выбрать исследование:", 
                            ["-------------------",
                             "Исследование номинальных зарплат за 2000-2023 гг.", 
                             "Исследование сред.зарплат с учетом уровня инфляции за 2000-2023 гг.",
                             "Анализ сред.зарплат в ДПИ, Строительстве, Образовании с учетом уровня инфляции за 2000-2023 гг.", 
                             "Изменение индексов ном. и реал. зарплат в ДПИ, Строительстве, Образовании за 2000-2023 гг.",
                             "Анализ сред.зарплат мужчин и женщин в ДПИ за 2005-2021 гг.",
                             "Анализ сред.зарплат мужчин и женщин в Строительстве за 2005-2021 гг.",
                             "Анализ сред.зарплат мужчин и женщин в Образовании за 2005-2021 гг."
                            ])

    if page == "-------------------":
        st.header("""Проект:  Анализ зарплат в России за период с 2000 по 2023 гг.""")
        st.write(
        """    
        ### Представлен анализ динамики уровня средних зарплат в разрезе по видам экономической деятельности `Добыча полезных ископаемых`,       `Строительство`, `Образование` в период с 2000 по 2023 гг.

        #### В проекте используются открытые данные из официальных источников:
          Сайт Росстата https://rosstat.gov.ru/

          Таблицы уровня инфляции в России https://уровень-инфляции.рф
        """
        )
        st.image(image)

    elif page == "Исследование номинальных зарплат за 2000-2023 гг.":
        st.header("""Изменения номинальных зарплат за 2000 - 2023 гг. по видам экономической деятельности: `Добыча полезных ископаемых`, `Строительство`, `Образование`
""")
        list_ser = ['добыча полезных ископаемых', 'строительство','образование' ]
        #width = st.sidebar.slider("Ширина графика", 10, 20, 10)
        #height = st.sidebar.slider("Высота графика", 10, 20, 10)
        fig, ax = plt.subplots()
        for i in list_ser:
             austr = data.loc[data['Economics_section'].eq(i)] # выбираем нужную строку данных
             d = austr.filter(regex=r"(?:20)\d\d").T.iloc[:, 0] # преобразовываем данные из широкого формата в высокий (транспонирование)
             d.plot()
        plt.legend(['добыча полезных ископаемых', 'строительство','образование' ], fontsize = 10)
        plt.title('Графики изменения зарплат за 2000 - 2023 гг. по видам экономической деятельности: Добыча полезных ископаемых, Строительство, Образование', fontsize = 10)
        plt.ylabel('Величина зарплаты, в рублях', fontsize = 10)
        plt.xlabel('Годы', fontsize = 10)
        st.pyplot(fig)
        st.write(
        """
        ### Вывод:
        Анализируя график, можно заметить:

        - заработная плата в области добычи полезных ископаемых растет существенно быстрее, чем в образовании и строительстве. К 2023 г. она  превосходит примерно в 2 раза рост зарплат по двум другим областям;

        - рост зарплаты в строительстве незначительно превышает рост зарплат в образовании, но в период с 2005 по 2014  рост заплаты в строительстве превышал рост зарплат в образовании, затем, примерно с 2013 г. их рост примерно выравнялся (что можно объяснить "майскими" указами и повышению зарплат, согласно им, в образовании) , а с 2020 г. наблюдается отрыв в росте зарплат в строительстве от зарплат в образовании.
        """         
        )
    elif page == "Исследование сред.зарплат с учетом уровня инфляции за 2000-2023 гг.":
         st.header("""Исследование средних зарплат с учетом уровня инфляции за 2000 - 2023 гг. по видам экономической деятельности: `Добыча полезных ископаемых`, `Строительство`, `Образование`
""")
         list_ser = ['добыча полезных ископаемых', 'строительство','образование']
         fig, ax = plt.subplots()
         for i in list_ser:
             austr = data.loc[data['Economics_section'].eq(i)] # выбираем нужную строку данных
             austr_2 = data_RS.loc[data['Economics_section'].eq(i)] # выбираем нужную строку данных
             d = austr.filter(regex=r"(?:20)\d\d").T.iloc[:, 0] # преобразовываем данные из широкого формата в высокий (транспонирование)
             d_2 = austr_2.filter(regex=r"(?:20)\d\d").T.iloc[:, 0]
             d.plot()
             d_2.plot()
         plt.legend(['добыча полезных ископаемых_НЗ','добыча полезных ископаемых_РЗ', 'строительство_НЗ','строительство_РЗ','образование_НЗ', 'образование_РЗ'])
         plt.title('Графики изменения номинальной и реальной зарплат за 2000 - 2023 гг. по видам экономической деятельности: Добыча полезных ископаемых, Строительство, Образование')
         plt.ylabel('Величина зарплаты, в рублях')
         plt.xlabel('Годы')
         st.pyplot(fig)
         st.write(
         """
         ### Вывод:
         Анализируя графики изменения номинальных и реальных зарплат в выбранных видах экономической деятельности  __Добыча полезных ископаемых__, __Строительство__, __Образование__ можно заметить:

         - реальные заработные платы отстают от  номинальных зарплат, что говорит о недостаточном уровне номинальных заработных плат, а именно так, чтобы их рост опережал рост инфляции;

         - можно выделить периоды, когда реальные зарплаты еще больше отличались от номинальных, а именно, это 2008-2009, 2014-2018г., и начавшийся примерно в 2022 г. новый период несоответствия.
         """
         )

    elif page == "Анализ сред.зарплат в ДПИ, Строительстве, Образовании с учетом уровня инфляции за 2000-2023 гг.":
        st.header("""Анализ средних зарплат в видах экономической деятельности `Добыча полезных ископаемых`, `Строительство`, `Образование` с учетом уровня инфляции за 2000-2023 гг. (графики по видам деятельности)""")
        fig, ax = plt.subplots()
        austr = data.loc[data['Economics_section'].eq('добыча полезных ископаемых')]   # выбираем нужную строку данных
        austr_2 = data_RS.loc[data['Economics_section'].eq('добыча полезных ископаемых')]   # выбираем нужную строку данных
        d = austr.filter(regex=r"(?:20)\d\d").T.iloc[:, 0]         # преобразовываем данные из широкого формата в высокий (транспонирование)
        d_2 = austr_2.filter(regex=r"(?:20)\d\d").T.iloc[:, 0]
        d.plot()
        d_2.plot()
        plt.legend(['Добыча полезных ископаемых_НЗ', 'Добыча полезных ископаемых_РЗ'])
        plt.title('Графики изменения номинальной и реальной зарплат за 2000-2023 гг. по виду экономической деятельности Добыча полезных ископаемых')
        plt.ylabel('Величина зарплаты, в рублях')
        plt.xlabel('Годы')
        st.pyplot(fig)

        fig, ax = plt.subplots()
        austr = data.loc[data['Economics_section'].eq('строительство')]   # выбираем нужную строку данных
        austr_2 = data_RS.loc[data['Economics_section'].eq('строительство')]   # выбираем нужную строку данных
        d = austr.filter(regex=r"(?:20)\d\d").T.iloc[:, 0]         # преобразовываем данные из широкого формата в высокий (транспонирование)
        d_2 = austr_2.filter(regex=r"(?:20)\d\d").T.iloc[:, 0]
        d.plot()
        d_2.plot()
        plt.legend(['Cтроительство_НЗ', 'Cтроительство_РЗ'])
        plt.title('Графики изменения номинальной и реальной зарплат за 2000-2023 гг. по виду экономической деятельности Cтроительство')
        plt.ylabel('Величина зарплаты, в рублях')
        plt.xlabel('Годы')
        st.pyplot(fig)

        fig, ax = plt.subplots()
        austr = data.loc[data['Economics_section'].eq('образование')]   # выбираем нужную строку данных
        austr_2 = data_RS.loc[data['Economics_section'].eq('образование')]   # выбираем нужную строку данных
        d = austr.filter(regex=r"(?:20)\d\d").T.iloc[:, 0]         # преобразовываем данные из широкого формата в высокий (транспонирование)
        d_2 = austr_2.filter(regex=r"(?:20)\d\d").T.iloc[:, 0]
        d.plot()
        d_2.plot()
        plt.legend(['Образование_НЗ', 'Образование_РЗ'])
        plt.title('Графики изменения номинальной и реальной зарплат за 2000-2023 гг. по виду экономической деятельности Образование')
        plt.ylabel('Величина зарплаты, в рублях')
        plt.xlabel('Годы')
        st.pyplot(fig)
        st.write(
         """
         ### Вывод:
         Анализируя графики изменения номинальных и реальных зарплат в выбранных видах экономической деятельности  __Добыча полезных ископаемых__, __Строительство__, __Образование__ можно заметить:

         - реальные заработные платы отстают от  номинальных зарплат, что говорит о недостаточном уровне номинальных заработных плат, а именно так, чтобы их рост опережал рост инфляции;

         - можно выделить периоды, когда реальные зарплаты еще больше отличались от номинальных, а именно, это 2008-2009, 2014-2018г., и начавшийся примерно в 2022 г. новый период несоответствия.
         """
         )

    elif page == "Изменение индексов ном. и реал. зарплат в ДПИ, Строительстве, Образовании за 2000-2023 гг.":
        st.header("""Изменение индексов номинальной  и реальной зарплат в видах экономической деятельности `Добыча полезных ископаемых`, `Строительство`, `Образование` за 2000-2023 гг.""")
        fig, ax = plt.subplots()
        austr = data_Ins.loc[data['Economics_section'].eq('добыча полезных ископаемых')]   # выбираем нужную строку данных
        austr_2 = data_Irs.loc[data['Economics_section'].eq('добыча полезных ископаемых')]   # выбираем нужную строку данных
        d = austr.filter(regex=r"(?:20)\d\d").T.iloc[:, 0]         # преобразовываем данные из широкого формата в высокий (транспонирование)
        d_2 = austr_2.filter(regex=r"(?:20)\d\d").T.iloc[:, 0]
        d.plot()
        d_2.plot()
        plt.legend(['Добыча полезных ископаемых_НЗ', 'Добыча полезных ископаемых_РЗ'])
        plt.title('Графики  измения индексов номинальной и реальной зарплат за 2000-2023 гг. по виду экономической деятельности Добыча полезных ископаемых')
        plt.ylabel('Значение индекса')
        plt.xlabel('Годы')
        st.pyplot(fig)

        fig, ax = plt.subplots()
        austr = data_Ins.loc[data['Economics_section'].eq('строительство')]   # выбираем нужную строку данных
        austr_2 = data_Irs.loc[data['Economics_section'].eq('строительство')]   # выбираем нужную строку данных
        d = austr.filter(regex=r"(?:20)\d\d").T.iloc[:, 0]         # преобразовываем данные из широкого формата в высокий (транспонирование)
        d_2 = austr_2.filter(regex=r"(?:20)\d\d").T.iloc[:, 0]
        d.plot()
        d_2.plot()
        plt.legend(['Cтроительство_НЗ', 'Cтроительство_РЗ'])
        plt.title('Графики изменения индексов номинальной и реальной зарплат за 2000-2023 гг. по виду экономической деятельности Cтроительство')
        plt.ylabel('Значение индекса')
        plt.xlabel('Годы')
        st.pyplot(fig)

        fig, ax = plt.subplots()
        austr = data_Ins.loc[data['Economics_section'].eq('образование')]   # выбираем нужную строку данных
        austr_2 = data_Irs.loc[data['Economics_section'].eq('образование')]   # выбираем нужную строку данных
        d = austr.filter(regex=r"(?:20)\d\d").T.iloc[:, 0]         # преобразовываем данные из широкого формата в высокий (транспонирование)
        d_2 = austr_2.filter(regex=r"(?:20)\d\d").T.iloc[:, 0]
        d.plot()
        d_2.plot()
        plt.legend(['Образование_НЗ', 'Образование_РЗ'])
        plt.title('Графики изменения индексов номинальной и реальной зарплат за 2000-2023 гг. по виду экономической деятельности Образование')
        plt.ylabel('Значение индекса')
        plt.xlabel('Годы')
        st.pyplot(fig)
        st.write(
         """
        ### Вывод:
        Графики измения индексов номинальной и реальной заработной платы являются одними из самых качественных показателей роста или падения заработной платы. В частности, по графику можно отследить, насколько, в действительности, уменьшается или увеличивается реальная заработная плата при увеличении или уменьшении номинальной зарплаты. 

        Кроме того:

        - во всех трех областях можно заметить быстрый рост зарплат, как номинальных, так и реальных, примерно с 2000 по 2003 год, однако затем резкое замедление роста зарплат примерно в 2004 г.;

        - такие резкие падения можно наблюдать в 2009-2010 и 2015 гг., а также быстрое падение реальных зарплат, начиная с 2022 г., особенно в Образовании и Добыче полезных ископаемых;

        - можно отметить более стабильное поведение зарплат в области Добычи полезных ископаемых, но постоянные скачики зарплат в Строительстве и Образовании, что вызвано, похоже, ситуативными вбрасываниями денежных масс с последующим урезанием.
         """
         )

    elif page == "Анализ сред.зарплат мужчин и женщин в ДПИ за 2005-2021 гг.":
        st.header("""Анализ средних зарплат мужчин и женщин по виду экономической деятельности `Добыча полезных ископаемых`за 2005-2021 гг.""")
        fig, ax = plt.subplots()
        austr = data_2005_2021.loc[data_2005_2021['Economics_section'].eq('добыча полезных ископаемых')]   # выбираем нужную строку данных
        austr_2 = MF_DPI.loc[MF_DPI['section'].eq('Мужчины')]
        austr_3 = MF_DPI.loc[MF_DPI['section'].eq('Женщины')]
        d = austr.filter(regex=r"(?:20)\d\d").T.iloc[:, 0]         # преобразовываем данные из широкого формата в высокий (транспонирование)
        d_2 = austr_2.filter(regex=r"(?:20)\d\d").T.iloc[:, 0]
        d_3 = austr_3.filter(regex=r"(?:20)\d\d").T.iloc[:, 0]
        d.plot()
        d_2.plot()
        d_3.plot()
        plt.legend(['Средн.зар.платы по ДПИ', 'Ср.зарплаты мужчин', 'Ср.зарплаты женщин'])
        plt.title('Средние зарплаты в целом, зарплаты мужчин и зарплаты женщин по виду экономической деятельности Добыча полезных ископаемых за 2005-2021 гг.')
        plt.ylabel('Величина зарплаты, в рублях')
        plt.xlabel('Годы')
        st.pyplot(fig)
        st.write(
        """
        ### Вывод:
        Анализ графиков показывает, что зарплаты женщин в виде экономической деятельности  __Добыча полезных ископаемых__ существенно ниже зарплат мужчин, а зарплаты мужчин близки к средним зарплатам. Спорным, правда, является тот факт, что средняя номинальная зарплата выше двух других, но это можно объяснить методологией нахождения средних зарплат мужчин и женщин - это выборочные зарплаты только за один осенний месяц, а номинальная зарплата берется за весь год.
        """
        )

    elif page == "Анализ сред.зарплат мужчин и женщин в Строительстве за 2005-2021 гг.":
        st.header("""Анализ средних зарплат мужчин и женщин по виду экономической деятельности `Строительство` за 2005-2021 гг.""")
        fig, ax = plt.subplots()
        austr = data_2005_2021.loc[data_2005_2021['Economics_section'].eq('строительство')]   # выбираем нужную строку данных
        austr_2 = MF_Str.loc[MF_Str['section'].eq('Мужчины')]
        austr_3 = MF_Str.loc[MF_Str['section'].eq('Женщины')]
        d = austr.filter(regex=r"(?:20)\d\d").T.iloc[:, 0]         # преобразовываем данные из широкого формата в высокий (транспонирование)
        d_2 = austr_2.filter(regex=r"(?:20)\d\d").T.iloc[:, 0]
        d_3 = austr_3.filter(regex=r"(?:20)\d\d").T.iloc[:, 0]
        d.plot()
        d_2.plot()
        d_3.plot()
        plt.legend(['Средн.зар.платы по Строительству', 'Ср.зарплаты мужчин', 'Ср.зарплаты женщин'])
        plt.title('Средние зарплаты в целом, зарплаты мужчин и зарплаты женщин по виду экономической деятельности Добыча полезных ископаемых за 2005 - 2021 гг.')
        plt.ylabel('Величина зарплаты, в рублях')
        plt.xlabel('Годы')
        st.pyplot(fig)
        st.write(
        """
        ### Вывод:
        Анализ графика зарплат мужчин и женщин в разделе экономики Строительство показывает, что уровень зарплат женщин ниже, чем у мужчин, однако , в целом, отклонение между ними примерно сохраняется в течение 17 лет, с небольшим всплеском в зарплатах женщин в 2017 г., когда они почти приблизились к зарплатам мужчин. Однако, сравнивая эти два графика с графиком номинальных зарплат, нужно сказать, что с 2013 г. номинальные зарплаты существенно отклоняются от сердних зарплат мужчин и женщин.

        Думаю, что это может быть связано с тем, номинальные зарплаты представлены за год в целом, а средние вязты только за один месяц, октябрь, в который, скорее всего, происходят максимальные выплаты за теплый период, и последующим "застоем" в течении холодного периода года, когда зарплаты минимальные.

         Почему это может быть связано именно с 2013 годом? Предлолагаю, что до 2012-2013 гг. не было большого строительного бума, и уровень зарплат распределялся более менее равномерно в течении года, конечно, с увеличением в теплое время года. Но строительный бум в послдние 10 лет, похоже, вызвал желание максимально обогатиться, пока есть возможность, и дал работникам возможность максимально заработать в летнее время.  
        """
        )

    elif page == "Анализ сред.зарплат мужчин и женщин в Образовании за 2005-2021 гг.":
        st.header("""Анализ средних зарплат мужчин и женщин по виду экономической деятельности `Образование` за 2005-2021 гг.""")
        fig, ax = plt.subplots()
        austr = data_2005_2021.loc[data_2005_2021['Economics_section'].eq('образование')]   # выбираем нужную строку данных
        austr_2 = MF_Ed.loc[MF_Ed['section'].eq('Мужчины')]
        austr_3 = MF_Ed.loc[MF_Ed['section'].eq('Женщины')]
        d = austr.filter(regex=r"(?:20)\d\d").T.iloc[:, 0]         # преобразовываем данные из широкого формата в высокий (транспонирование)
        d_2 = austr_2.filter(regex=r"(?:20)\d\d").T.iloc[:, 0]
        d_3 = austr_3.filter(regex=r"(?:20)\d\d").T.iloc[:, 0]
        d.plot()
        d_2.plot()
        d_3.plot()
        plt.legend(['Средн.зар.платы по Образованию', 'Ср.зарплаты мужчин', 'Ср.зарплаты женщин'])
        plt.title('Средние зарплаты в целом, зарплаты мужчин и зарплаты женщин по виду экономической деятельности Добыча полезных ископаемых за 2005-2021 гг.')
        plt.ylabel('Величина зарплаты, в рублях')
        plt.xlabel('Годы')
        st.pyplot(fig)
        st.write(
        """
        ### Вывод:
        Анализ графиков для вида экономической деятельности __Образование__ показывает, что, в целом, номинальные зарплаты и зарплаты мужчин и женщин отличаются незначительно. С 2005 по 2012 гг. средние зарплаты мужчин даже превосходили средние номинальные зарплаты по разделу. 

        Зарплаты женщин меньше, чем зарплаты мужчин, за исключением 2013 г., когда они совпали. С 2017 г. уровень средних номинальных зарплат стал превосходить средние зарплаты мужчин и женщин в этот период, что, отчасти, также может быть вызвано использованием только одного месяца в качестве усредненных данных.
        """
        )



if __name__ == "__main__":
          main()