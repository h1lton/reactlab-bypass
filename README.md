<a name="readme-top"></a>
<br>
<div align="center">
  <a href="https://github.com/h1lton/reactlab-bypass">
    <img src="https://cdn-icons-png.flaticon.com/512/4248/4248418.png " width="100" height="100" alt="Logo">
  </a>
  <h3>React Lab Bypass</h3>
  <p>
    Обход защиты React Lab на Python
    <br>
    <a href="https://github.com/h1lton/reactlab-bypass"><strong>Explore the docs »</strong></a>
    <br>
    <br>
  </p>

  <img src="https://skillicons.dev/icons?i=py,githubactions&theme=light" alt="Tech">

  <p>
    <br>
    <a href="https://github.com/h1lton/reactlab-bypass">View Demo</a>
    ·
    <a href="https://github.com/h1lton/reactlab-bypass/issues">Report Bug</a>
    ·
    <a href="https://github.com/h1lton/reactlab-bypass/issues">Request Feature</a>
  </p>
</div>


<details>
  <summary>Оглавление</summary>
  <ol>
    <li><a href="#стек-технологий">Стек технологий</a></li>
    <li><a href="#установка">Установка</a></li>
    <li><a href="#использование">Использование</a></li>
  </ol>
</details>

## Стек технологий

- <img src="https://skillicons.dev/icons?i=py&theme=light" alt="icon" style="width: 25px"> Python 3.11.7
- <img src="https://skillicons.dev/icons?i=py&theme=light" alt="icon" style="width: 25px"> Requests 2.31.0
- <img src="https://skillicons.dev/icons?i=py&theme=light" alt="icon" style="width: 25px"> Pycryptodome 3.20.0

<p align="right">(<a href="#readme-top">вернуться наверх</a>)</p>

# Установка

1. Клонируйте репозиторий
   ```sh
   git clone https://github.com/h1lton/url-shortener.git
   cd url-shortener
   ```
2. Создайте виртуальное окружение
   ```sh
   python -m venv venv
   ```
3. Активируйте виртуальное окружение
   ```sh
   venv\Scripts\activate
   ```
4. Установите зависимости
   ```sh
   pip install -r requirements.txt
   ```

или вставьте файл main.py в свой проект, и установите нужные зависимости: Requests и Pycryptodome.

<p align="right">(<a href="#readme-top">вернуться наверх</a>)</p>

## Использование

```python
import requests
from main import ReactLabBypass

your_site = "https://radmir.online"
rlb = ReactLabBypass(your_site)

response = requests.get(your_site, headers={"cookie": rlb.get_cookie()})
# ...
response = requests.get(your_site + "/forbes", headers={"cookie": rlb.get_cookie()})
# ...
```

### Пример сохранения данных

```python
# ...
your_cache_module.set("rl.cookie", rlb.get_cookie())
your_cache_module.set("rl.cookie_expires_at", rlb.cookie_expires_at)
```

### Пример использования с уже ранее полученными данными

```python
# ...
rlb = ReactLabBypass(
   your_site,
   cookie=your_cache_module.get("rl.cookie"),
   cookie_expires_at=your_cache_module.get("rl.cookie_expires_at")
)

response = requests.get(your_site, headers={"cookie": rlb.get_cookie()})
# ...
```

В коде есть комментарии, можете взглянуть для продвинутого использования.
<p align="right">(<a href="#readme-top">вернуться наверх</a>)</p>
