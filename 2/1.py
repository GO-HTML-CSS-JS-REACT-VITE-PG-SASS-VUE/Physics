import os
import webbrowser
from pathlib import Path

def create_physics_website():
    # Создаем структуру папок
    base_dir = Path("physics_9_grade")
    topics_dir = base_dir / "topics"
    
    # Основные разделы и их темы
    sections = {
        "mechanics": {
            "title": "Механика",
            "topics": [
                "kinematika", "dinamika", "statika", 
                "newton_laws", "circular_motion", "impulse_conservation"
            ]
        },
        "thermal": {
            "title": "Тепловые явления",
            "topics": [
                "temperature", "heat_transfer", "gas_laws",
                "thermodynamics", "heat_engines"
            ]
        },
        "electromagnetism": {
            "title": "Электромагнетизм",
            "topics": [
                "electric_field", "current_laws", "magnetic_field",
                "induction", "oscillations", "waves"
            ]
        },
        "optics": {
            "title": "Оптика",
            "topics": [
                "reflection_refraction", "lenses", "optical_instruments",
                "wave_properties", "dispersion"
            ]
        },
        "quantum": {
            "title": "Квантовая физика",
            "topics": [
                "photoeffect", "atom_structure", "nuclear_reactions",
                "radioactivity", "elementary_particles"
            ]
        }
    }
    
    # Создаем директории
    topics_dir.mkdir(parents=True, exist_ok=True)
    for section in sections.keys():
        (topics_dir / section).mkdir(exist_ok=True)
    
    # Создаем HTML файлы для каждой темы
    create_topic_pages(topics_dir, sections)
    
    # Создаем главную страницу
    create_main_page(base_dir, sections)
    
    # Запускаем в браузере
    webbrowser.open(f'file://{base_dir / "index.html"}')

def create_main_page(base_dir, sections):
    html_content = '''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Физика 9 класс - Интерактивный справочник</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: 'Segoe UI', system-ui, sans-serif; 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            min-height: 100vh;
        }
        .header {
            text-align: center;
            color: white;
            margin-bottom: 30px;
        }
        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        .header p {
            font-size: 1.2em;
            opacity: 0.9;
        }
        .accordion { 
            max-width: 900px; 
            margin: 0 auto; 
        }
        .section { 
            background: white; 
            border-radius: 15px; 
            margin-bottom: 20px; 
            box-shadow: 0 8px 25px rgba(0,0,0,0.15); 
            overflow: hidden;
            transition: transform 0.3s ease;
        }
        .section:hover {
            transform: translateY(-5px);
        }
        .section-header { 
            padding: 25px; 
            cursor: pointer; 
            display: flex; 
            justify-content: space-between; 
            align-items: center; 
            font-weight: 600; 
            font-size: 20px; 
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
            transition: all 0.3s ease;
        }
        .section-header:hover { 
            background: linear-gradient(135deg, #f5576c 0%, #f093fb 100%);
        }
        .section-header::after { 
            content: "+"; 
            font-size: 24px; 
            font-weight: bold;
            transition: all 0.3s ease; 
        }
        .section.active .section-header::after { 
            content: "-"; 
        }
        .topics { 
            padding: 0 25px; 
            max-height: 0; 
            overflow: hidden; 
            transition: max-height 0.5s ease; 
        }
        .section.active .topics { 
            max-height: 600px; 
            padding: 20px 25px 25px; 
        }
        .topic-list { 
            list-style: none; 
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 15px;
        }
        .topic-list li { 
            background: #f8f9fa;
            border-radius: 10px;
            transition: all 0.3s ease;
        }
        .topic-list li:hover {
            background: #e9ecef;
            transform: scale(1.05);
        }
        .topic-link { 
            color: #495057; 
            text-decoration: none; 
            display: block;
            padding: 15px 20px;
            font-weight: 500;
            transition: color 0.3s ease;
        }
        .topic-link:hover { 
            color: #667eea; 
        }
        .footer {
            text-align: center;
            color: white;
            margin-top: 40px;
            opacity: 0.8;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🧪 Физика 9 класс</h1>
        <p>Интерактивный справочник с формулами и объяснениями</p>
    </div>
    
    <div class="accordion">
'''
    
    # Добавляем разделы
    for section_id, section_data in sections.items():
        html_content += f'''
        <div class="section">
            <div class="section-header">{section_data['title']}</div>
            <div class="topics">
                <ul class="topic-list">'''
        
        for topic in section_data['topics']:
            topic_name_ru = get_topic_name_ru(topic)
            html_content += f'''
                    <li><a href="topics/{section_id}/{topic}.html" class="topic-link">{topic_name_ru}</a></li>'''
        
        html_content += '''
                </ul>
            </div>
        </div>'''
    
    html_content += '''
    </div>

    <div class="footer">
        <p>Изучайте физику с удовольствием! 📚✨</p>
    </div>

    <script>
        document.querySelectorAll('.section-header').forEach(header => {
            header.addEventListener('click', () => {
                const section = header.parentElement;
                const isActive = section.classList.contains('active');
                
                // Закрываем все открытые разделы
                document.querySelectorAll('.section.active').forEach(activeSection => {
                    if (activeSection !== section) {
                        activeSection.classList.remove('active');
                    }
                });
                
                // Переключаем текущий раздел
                section.classList.toggle('active', !isActive);
            });
        });
    </script>
</body>
</html>'''
    
    with open(base_dir / "index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

def create_topic_pages(topics_dir, sections):
    topic_content = {
        # Механика
        "kinematika": {
            "title": "Кинематика",
            "formulas": [
                {"formula": "v = s/t", "explanation": "Скорость = путь / время. Средняя скорость движения"},
                {"formula": "a = (v - v₀)/t", "explanation": "Ускорение = изменение скорости / время. Показывает как быстро меняется скорость"},
                {"formula": "s = v₀t + at²/2", "explanation": "Путь при равноускоренном движении. Зависит от начальной скорости и ускорения"}
            ],
            "description": "🎯 <strong>Кинематика</strong> - это раздел механики, изучающий движение тел без рассмотрения причин этого движения. Здесь мы описываем <em>как</em> движется тело, но не <em>почему</em>.",
            "fun_fact": "💡 Знаете ли вы? Самый быстрый наземный объект - гиперзвуковая ракета - развивает скорость до 10 Махов (12 000 км/ч)!",
            "examples": [
                "Автомобиль проехал 120 км за 2 часа - его средняя скорость 60 км/ч",
                "Тело начинает двигаться с ускорением 2 м/с² - через 5 секунд его скорость будет 10 м/с"
            ]
        },
        "dinamika": {
            "title": "Динамика", 
            "formulas": [
                {"formula": "F = ma", "explanation": "Второй закон Ньютона: сила = масса × ускорение. Основной закон динамики!"},
                {"formula": "P = mg", "explanation": "Вес тела = масса × ускорение свободного падения. На Земле g ≈ 9.8 м/с²"},
                {"formula": "F₁₂ = -F₂₁", "explanation": "Третий закон Ньютона: силы действия и противодействия равны и противоположны"}
            ],
            "description": "⚡ <strong>Динамика</strong> изучает причины движения тел. Здесь мы отвечаем на вопрос: <em>«Почему тела движутся именно так?»</em>",
            "fun_fact": "🚀 Чтобы оторваться от Земли, ракете нужно преодолеть силу тяжести - для этого требуется огромная сила тяги!",
            "examples": [
                "Чем больше сила, приложенная к телу, тем больше его ускорение",
                "Ваш вес на Луне будет в 6 раз меньше из-за меньшей гравитации"
            ]
        },
        "newton_laws": {
            "title": "Законы Ньютона",
            "formulas": [
                {"formula": "F = 0 ⇒ v = const", "explanation": "Первый закон: если нет сил, тело сохраняет скорость. Закон инерции!"},
                {"formula": "F = ma", "explanation": "Второй закон: сила определяет ускорение тела"},
                {"formula": "F₁₂ = -F₂₁", "explanation": "Третий закон: сила действия равна силе противодействия"}
            ],
            "description": "🎓 <strong>Три закона Ньютона</strong> - основа классической механики. Они описывают движение тел под действием сил.",
            "fun_fact": "🍎 По легенде, Ньютон открыл закон всемирного тяготения, когда ему на голову упало яблоко!",
            "examples": [
                "Мяч продолжает лететь после удара - работает первый закон",
                "Чем сильнее вы толкаете тележку, тем быстрее она едет - второй закон",
                "При выстреле ружье отдает в плечо - третий закон"
            ]
        },
        # Тепловые явления
        "temperature": {
            "title": "Температура и тепловое равновесие",
            "formulas": [
                {"formula": "T(K) = T(°C) + 273", "explanation": "Перевод градусов Цельсия в Кельвины. Абсолютный ноль: -273°C"},
                {"formula": "Q = cmΔT", "explanation": "Количество теплоты = удельная теплоемкость × масса × изменение температуры"}
            ],
            "description": "🌡️ <strong>Температура</strong> - мера средней кинетической энергии молекул. При тепловом равновесии температуры выравниваются.",
            "fun_fact": "❄️ Абсолютный ноль (-273°C) - самая низкая возможная температура. При ней прекращается движение молекул!",
            "examples": [
                "Горячий чай остывает в комнате до комнатной температуры",
                "Для нагрева 1 кг воды на 1°C нужно 4200 Дж теплоты"
            ]
        },
        "gas_laws": {
            "title": "Уравнение состояния идеального газа",
            "formulas": [
                {"formula": "PV = nRT", "explanation": "Уравнение Менделеева-Клапейрона: давление × объем = количество вещества × газовая постоянная × температура"},
                {"formula": "P = nkT", "explanation": "Давление = концентрация молекул × постоянная Больцмана × температура"}
            ],
            "description": "💨 <strong>Идеальный газ</strong> - математическая модель, где молекулы - материальные точки без взаимодействия.",
            "fun_fact": "🎈 Воздушный шар на холоде сжимается, а на жаре расширяется - это работает закон Шарля!",
            "examples": [
                "При сжатии газа в шприце его давление увеличивается",
                "Нагретый воздух в воздушном шаре делает его легче"
            ]
        },
        # Электромагнетизм
        "electric_field": {
            "title": "Электрическое поле",
            "formulas": [
                {"formula": "F = kq₁q₂/r²", "explanation": "Закон Кулона: сила взаимодействия зарядов пропорциональна их величинам и обратно пропорциональна квадрату расстояния"},
                {"formula": "E = F/q", "explanation": "Напряженность поля = сила, действующая на заряд / величина заряда"},
                {"formula": "φ = kq/r", "explanation": "Потенциал поля точечного заряда"}
            ],
            "description": "⚡ <strong>Электрическое поле</strong> - особый вид материи, окружающей заряженные тела. Оно действует на другие заряды.",
            "fun_fact": "🌩️ Молния - это гигантский электрический разряд напряжением до 1 миллиарда вольт!",
            "examples": [
                "Два одноименных заряда отталкиваются, разноименные - притягиваются",
                "Напряженность поля убывает с расстоянием от заряда"
            ]
        },
        "current_laws": {
            "title": "Законы постоянного тока",
            "formulas": [
                {"formula": "I = U/R", "explanation": "Закон Ома: сила тока = напряжение / сопротивление. Основной закон электрических цепей!"},
                {"formula": "P = UI", "explanation": "Мощность тока = напряжение × сила тока"},
                {"formula": "Q = I²Rt", "explanation": "Закон Джоуля-Ленца: количество теплоты = квадрат тока × сопротивление × время"}
            ],
            "description": "🔌 <strong>Постоянный ток</strong> - упорядоченное движение зарядов в одном направлении.",
            "fun_fact": "💡 Лампочка мощностью 100 Вт за 10 часов работы потребляет 1 кВт·ч электроэнергии",
            "examples": [
                "Чем больше сопротивление, тем меньше ток при том же напряжении",
                "Провода нагреваются при прохождении тока - работает закон Джоуля-Ленца"
            ]
        },
        # Оптика
        "lenses": {
            "title": "Линзы",
            "formulas": [
                {"formula": "1/F = 1/f + 1/d", "explanation": "Формула тонкой линзы: 1/фокусное расстояние = 1/расстояние до изображения + 1/расстояние до объекта"},
                {"formula": "Γ = f/d", "explanation": "Увеличение линзы = фокусное расстояние / расстояние до объекта"}
            ],
            "description": "🔍 <strong>Линзы</strong> - прозрачные тела, ограниченные сферическими поверхностями. Они преломляют свет и формируют изображения.",
            "fun_fact": "👁️ Человеческий глаз - это сложная линза, которая может автоматически настраивать фокус!",
            "examples": [
                "Собирающие линзы увеличивают изображения",
                "Рассеивающие линзы уменьшают изображения"
            ]
        },
        # Квантовая физика
        "photoeffect": {
            "title": "Фотоэффект",
            "formulas": [
                {"formula": "hν = A + mv²/2", "explanation": "Уравнение Эйнштейна для фотоэффекта: энергия фотона = работа выхода + кинетическая энергия электрона"},
                {"formula": "E = hν", "explanation": "Энергия фотона = постоянная Планка × частота света"}
            ],
            "description": "🌟 <strong>Фотоэффект</strong> - явление вырывания электронов из вещества под действием света. Подтверждает квантовую природу света.",
            "fun_fact": "🎖️ За объяснение фотоэффекта Эйнштейн получил Нобелевскую премию в 1921 году!",
            "examples": [
                "Солнечные батареи работают на принципе фотоэффекта",
                "Для каждого вещества есть минимальная частота света, вызывающая фотоэффект"
            ]
        }
    }
    
    # Заполняем недостающие темы
    for section_id, section_data in sections.items():
        for topic in section_data['topics']:
            if topic not in topic_content:
                topic_content[topic] = {
                    "title": get_topic_name_ru(topic),
                    "formulas": [{"formula": "Основные формулы...", "explanation": "Подробное объяснение формулы"}],
                    "description": "📚 <strong>Интересная информация</strong> по этой теме будет добавлена в ближайшее время!",
                    "fun_fact": "💫 Эта тема содержит много удивительных фактов о физике нашего мира!",
                    "examples": ["Примеры применения знаний на практике"]
                }
    
    # Создаем HTML файлы для каждой темы
    for section_id, section_data in sections.items():
        for topic in section_data['topics']:
            content = topic_content[topic]
            create_topic_html(topics_dir / section_id / f"{topic}.html", content)

def create_topic_html(file_path, content):
    formulas_html = ""
    for item in content['formulas']:
        formulas_html += f'''
            <div class="formula-item">
                <div class="formula">{item['formula']}</div>
                <div class="explanation">💡 {item['explanation']}</div>
            </div>'''
    
    examples_html = ""
    for example in content.get('examples', []):
        examples_html += f'<li>📌 {example}</li>'
    
    html = f'''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{content['title']} - Физика 9 класс</title>
    <style>
        body {{ 
            font-family: 'Segoe UI', system-ui, sans-serif; 
            margin: 0; 
            padding: 20px; 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }}
        .container {{ 
            max-width: 900px; 
            margin: 0 auto; 
            background: white; 
            padding: 40px; 
            border-radius: 20px; 
            box-shadow: 0 15px 35px rgba(0,0,0,0.2);
        }}
        h1 {{ 
            color: #667eea; 
            margin-bottom: 20px;
            font-size: 2.2em;
            border-bottom: 3px solid #667eea;
            padding-bottom: 10px;
        }}
        .back-btn {{ 
            display: inline-flex;
            align-items: center;
            margin-bottom: 25px; 
            color: #667eea; 
            text-decoration: none;
            font-weight: 500;
            padding: 10px 20px;
            background: #f8f9fa;
            border-radius: 10px;
            transition: all 0.3s ease;
        }}
        .back-btn:hover {{
            background: #667eea;
            color: white;
            transform: translateX(-5px);
        }}
        .description {{ 
            line-height: 1.7; 
            color: #555; 
            font-size: 1.1em;
            margin-bottom: 30px;
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            border-left: 4px solid #667eea;
        }}
        .formulas {{ 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 25px; 
            border-radius: 15px; 
            margin: 30px 0; 
            color: white;
        }}
        .formula-item {{
            margin: 20px 0;
            padding: 15px;
            background: rgba(255,255,255,0.1);
            border-radius: 10px;
            backdrop-filter: blur(10px);
        }}
        .formula {{ 
            font-family: 'Courier New', monospace; 
            font-size: 22px; 
            font-weight: bold;
            margin: 10px 0; 
            color: #fff;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
        }}
        .explanation {{
            font-size: 1em;
            opacity: 0.9;
            margin-top: 8px;
        }}
        .fun-fact {{
            background: #fff3cd;
            border: 2px solid #ffeaa7;
            border-radius: 12px;
            padding: 20px;
            margin: 25px 0;
            color: #856404;
        }}
        .examples {{
            background: #d1ecf1;
            border-radius: 12px;
            padding: 20px;
            margin: 25px 0;
        }}
        .examples ul {{
            margin: 10px 0;
            padding-left: 20px;
        }}
        .examples li {{
            margin: 8px 0;
            line-height: 1.5;
        }}
    </style>
</head>
<body>
    <div class="container">
        <a href="../../index.html" class="back-btn">← Назад к списку тем</a>
        <h1>🎯 {content['title']}</h1>
        
        <div class="description">
            {content['description']}
        </div>
        
        <div class="fun-fact">
            <strong>🎪 Интересный факт:</strong> {content.get('fun_fact', 'Узнавайте новое каждый день!')}
        </div>
        
        <div class="formulas">
            <h3 style="color: white; margin-top: 0;">🧮 Основные формулы и законы:</h3>
            {formulas_html}
        </div>
        
        <div class="examples">
            <h3 style="color: #0c5460; margin-top: 0;">🔍 Примеры и применение:</h3>
            <ul>
                {examples_html}
            </ul>
        </div>
    </div>
</body>
</html>'''
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)

def get_topic_name_ru(topic_key):
    names = {
        "kinematika": "Кинематика",
        "dinamika": "Динамика", 
        "statika": "Статика",
        "newton_laws": "Законы Ньютона",
        "circular_motion": "Движение по окружности",
        "impulse_conservation": "Закон сохранения импульса",
        "temperature": "Температура и тепловое равновесие",
        "heat_transfer": "Теплопередача",
        "gas_laws": "Уравнение состояния идеального газа",
        "thermodynamics": "Первый закон термодинамики",
        "heat_engines": "Тепловые двигатели",
        "electric_field": "Электрическое поле",
        "current_laws": "Законы постоянного тока",
        "magnetic_field": "Магнитное поле",
        "induction": "Электромагнитная индукция",
        "oscillations": "Электромагнитные колебания",
        "waves": "Электромагнитные волны",
        "reflection_refraction": "Отражение и преломление света",
        "lenses": "Линзы",
        "optical_instruments": "Оптические приборы",
        "wave_properties": "Волновые свойства света",
        "dispersion": "Дисперсия света",
        "photoeffect": "Фотоэффект",
        "atom_structure": "Строение атома",
        "nuclear_reactions": "Ядерные реакции",
        "radioactivity": "Радиоактивность",
        "elementary_particles": "Элементарные частицы"
    }
    return names.get(topic_key, topic_key)

if __name__ == "__main__":
    create_physics_website()
    print("🚀 Интерактивный сайт по физике создан!")
    print("📁 Папка: physics_9_grade")
    print("🌐 Запускаю в браузере...")