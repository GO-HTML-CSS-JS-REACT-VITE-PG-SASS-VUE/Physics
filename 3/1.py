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
    <title>Физика 9 класс</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: Arial, sans-serif; background: #f5f5f5; padding: 20px; }
        .accordion { max-width: 800px; margin: 0 auto; }
        .section { background: white; border: 1px solid #ddd; margin-bottom: 10px; }
        .section-header { padding: 15px; cursor: pointer; display: flex; justify-content: space-between; align-items: center; font-weight: bold; background: #f0f0f0; }
        .section-header::after { content: "+"; }
        .section.active .section-header::after { content: "-"; }
        .topics { padding: 0 15px; max-height: 0; overflow: hidden; transition: max-height 0.3s ease; }
        .section.active .topics { max-height: 500px; padding: 15px; }
        .topic-list { list-style: none; }
        .topic-list li { padding: 8px 0; border-bottom: 1px solid #eee; }
        .topic-list li:last-child { border-bottom: none; }
        .topic-link { color: #333; text-decoration: none; }
        .topic-link:hover { color: #0066cc; }
    </style>
</head>
<body>
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

    <script>
        document.querySelectorAll('.section-header').forEach(header => {
            header.addEventListener('click', () => {
                const section = header.parentElement;
                section.classList.toggle('active');
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
                {"formula": "v = s/t", "explanation": "Скорость = путь / время"},
                {"formula": "a = (v - v₀)/t", "explanation": "Ускорение = изменение скорости / время"},
                {"formula": "s = v₀t + at²/2", "explanation": "Путь при равноускоренном движении"}
            ],
            "description": "Кинематика изучает движение тел без рассмотрения причин этого движения."
        },
        "dinamika": {
            "title": "Динамика", 
            "formulas": [
                {"formula": "F = ma", "explanation": "Второй закон Ньютона: сила = масса × ускорение"},
                {"formula": "P = mg", "explanation": "Вес тела = масса × ускорение свободного падения"},
                {"formula": "F₁₂ = -F₂₁", "explanation": "Третий закон Ньютона"}
            ],
            "description": "Динамика изучает причины движения тел."
        },
        "newton_laws": {
            "title": "Законы Ньютона",
            "formulas": [
                {"formula": "F = 0 ⇒ v = const", "explanation": "Первый закон: если нет сил, тело сохраняет скорость"},
                {"formula": "F = ma", "explanation": "Второй закон: сила определяет ускорение"},
                {"formula": "F₁₂ = -F₂₁", "explanation": "Третий закон: сила действия равна силе противодействия"}
            ],
            "description": "Три закона Ньютона - основа классической механики."
        },
        # Тепловые явления
        "temperature": {
            "title": "Температура и тепловое равновесие",
            "formulas": [
                {"formula": "T(K) = T(°C) + 273", "explanation": "Перевод градусов Цельсия в Кельвины"},
                {"formula": "Q = cmΔT", "explanation": "Количество теплоты = удельная теплоемкость × масса × изменение температуры"}
            ],
            "description": "Температура - мера средней кинетической энергии молекул."
        },
        "gas_laws": {
            "title": "Уравнение состояния идеального газа",
            "formulas": [
                {"formula": "PV = nRT", "explanation": "Уравнение Менделеева-Клапейрона"},
                {"formula": "P = nkT", "explanation": "Давление = концентрация молекул × постоянная Больцмана × температура"}
            ],
            "description": "Идеальный газ - математическая модель, где молекулы - материальные точки без взаимодействия."
        },
        # Электромагнетизм
        "electric_field": {
            "title": "Электрическое поле",
            "formulas": [
                {"formula": "F = kq₁q₂/r²", "explanation": "Закон Кулона"},
                {"formula": "E = F/q", "explanation": "Напряженность поля = сила / величина заряда"},
                {"formula": "φ = kq/r", "explanation": "Потенциал поля точечного заряда"}
            ],
            "description": "Электрическое поле - вид материи, окружающей заряженные тела."
        },
        "current_laws": {
            "title": "Законы постоянного тока",
            "formulas": [
                {"formula": "I = U/R", "explanation": "Закон Ома"},
                {"formula": "P = UI", "explanation": "Мощность тока = напряжение × сила тока"},
                {"formula": "Q = I²Rt", "explanation": "Закон Джоуля-Ленца"}
            ],
            "description": "Постоянный ток - упорядоченное движение зарядов в одном направлении."
        },
        # Оптика
        "lenses": {
            "title": "Линзы",
            "formulas": [
                {"formula": "1/F = 1/f + 1/d", "explanation": "Формула тонкой линзы"},
                {"formula": "Γ = f/d", "explanation": "Увеличение линзы"}
            ],
            "description": "Линзы - прозрачные тела, ограниченные сферическими поверхностями."
        },
        # Квантовая физика
        "photoeffect": {
            "title": "Фотоэффект",
            "formulas": [
                {"formula": "hν = A + mv²/2", "explanation": "Уравнение Эйнштейна для фотоэффекта"},
                {"formula": "E = hν", "explanation": "Энергия фотона"}
            ],
            "description": "Фотоэффект - явление вырывания электронов из вещества под действием света."
        }
    }
    
    # Заполняем недостающие темы
    for section_id, section_data in sections.items():
        for topic in section_data['topics']:
            if topic not in topic_content:
                topic_content[topic] = {
                    "title": get_topic_name_ru(topic),
                    "formulas": [{"formula": "Формула", "explanation": "Объяснение формулы"}],
                    "description": "Описание темы"
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
                <div class="explanation">{item['explanation']}</div>
            </div>'''
    
    html = f'''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{content['title']}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 0; padding: 20px; background: #f5f5f5; }}
        .container {{ max-width: 800px; margin: 0 auto; background: white; padding: 20px; border: 1px solid #ddd; }}
        h1 {{ margin-bottom: 20px; color: #333; }}
        .back-btn {{ display: inline-block; margin-bottom: 20px; color: #0066cc; text-decoration: none; }}
        .description {{ margin-bottom: 20px; line-height: 1.5; color: #555; }}
        .formulas {{ border-top: 1px solid #ddd; padding-top: 20px; }}
        .formula-item {{ margin-bottom: 15px; }}
        .formula {{ font-family: monospace; font-size: 16px; margin-bottom: 5px; }}
        .explanation {{ color: #666; font-size: 14px; }}
    </style>
</head>
<body>
    <div class="container">
        <a href="../../index.html" class="back-btn">← Назад</a>
        <h1>{content['title']}</h1>
        
        <div class="description">
            {content['description']}
        </div>
        
        <div class="formulas">
            <h3>Формулы:</h3>
            {formulas_html}
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
    print("Сайт по физике создан!")