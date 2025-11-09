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
        body { font-family: system-ui, sans-serif; background: #f5f7fa; padding: 20px; }
        .accordion { max-width: 800px; margin: 0 auto; }
        .section { background: white; border-radius: 12px; margin-bottom: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); overflow: hidden; }
        .section-header { padding: 20px; cursor: pointer; display: flex; justify-content: space-between; align-items: center; font-weight: 600; font-size: 18px; transition: background 0.3s; }
        .section-header:hover { background: #f8f9fa; }
        .section-header::after { content: "+"; font-size: 18px; transition: transform 0.3s; color: #667eea; }
        .section.active .section-header::after { content: "-"; }
        .topics { padding: 0 20px; max-height: 0; overflow: hidden; transition: max-height 0.3s ease; }
        .section.active .topics { max-height: 500px; padding: 0 20px 20px; }
        .topic-list { list-style: none; }
        .topic-list li { padding: 10px 0; border-bottom: 1px solid #eee; }
        .topic-list li:last-child { border-bottom: none; }
        .topic-link { color: #555; text-decoration: none; display: block; transition: color 0.3s; }
        .topic-link:hover { color: #667eea; }
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
            "formulas": ["v = s/t", "a = (v - v₀)/t", "s = v₀t + at²/2"],
            "description": "Раздел механики, изучающий движение тел без рассмотрения причин этого движения."
        },
        "dinamika": {
            "title": "Динамика", 
            "formulas": ["F = ma", "P = mg", "F₁₂ = -F₂₁"],
            "description": "Раздел механики, изучающий причины возникновения движения."
        },
        "newton_laws": {
            "title": "Законы Ньютона",
            "formulas": ["1. F=0 ⇒ v=const", "2. F=ma", "3. F₁₂=-F₂₁"],
            "description": "Основные законы классической механики."
        },
        # Тепловые явления
        "temperature": {
            "title": "Температура и тепловое равновесие",
            "formulas": ["T(K) = T(°C) + 273", "Q = cmΔT"],
            "description": "Температура - мера средней кинетической энергии молекул."
        },
        "gas_laws": {
            "title": "Уравнение состояния идеального газа",
            "formulas": ["PV = nRT", "P = nkT"],
            "description": "Уравнение Менделеева-Клапейрона описывает состояние идеального газа."
        },
        # Электромагнетизм
        "electric_field": {
            "title": "Электрическое поле",
            "formulas": ["F = kq₁q₂/r²", "E = F/q", "φ = kq/r"],
            "description": "Электрическое поле - вид материи, окружающей заряженные тела."
        },
        "current_laws": {
            "title": "Законы постоянного тока",
            "formulas": ["I = U/R", "P = UI", "Q = I²Rt"],
            "description": "Закон Ома и другие законы постоянного электрического тока."
        },
        # Оптика
        "lenses": {
            "title": "Линзы",
            "formulas": ["1/F = 1/f + 1/d", "Γ = f/d"],
            "description": "Линзы - прозрачные тела, ограниченные сферическими поверхностями."
        },
        # Квантовая физика
        "photoeffect": {
            "title": "Фотоэффект",
            "formulas": ["hν = A + mv²/2", "E = hν"],
            "description": "Явление вырывания электронов из вещества под действием света."
        }
    }
    
    # Заполняем недостающие темы
    for section_id, section_data in sections.items():
        for topic in section_data['topics']:
            if topic not in topic_content:
                topic_content[topic] = {
                    "title": get_topic_name_ru(topic),
                    "formulas": ["Формулы по теме..."],
                    "description": "Описание темы..."
                }
    
    # Создаем HTML файлы для каждой темы
    for section_id, section_data in sections.items():
        for topic in section_data['topics']:
            content = topic_content[topic]
            create_topic_html(topics_dir / section_id / f"{topic}.html", content)

def create_topic_html(file_path, content):
    html = f'''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{content['title']}</title>
    <style>
        body {{ font-family: system-ui, sans-serif; margin: 0; padding: 20px; background: #f5f7fa; }}
        .container {{ max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }}
        h1 {{ color: #667eea; margin-bottom: 20px; }}
        .back-btn {{ display: inline-block; margin-bottom: 20px; color: #667eea; text-decoration: none; }}
        .formulas {{ background: #f8f9fa; padding: 20px; border-radius: 8px; margin: 20px 0; }}
        .formula {{ font-family: monospace; font-size: 18px; margin: 10px 0; }}
        .description {{ line-height: 1.6; color: #555; }}
    </style>
</head>
<body>
    <div class="container">
        <a href="../../index.html" class="back-btn">← Назад к списку тем</a>
        <h1>{content['title']}</h1>
        
        <div class="description">
            <p>{content['description']}</p>
        </div>
        
        <div class="formulas">
            <h3>Основные формулы:</h3>
            {''.join(f'<div class="formula">{formula}</div>' for formula in content['formulas'])}
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
    print("Сайт по физике создан! Запускаю в браузере...")