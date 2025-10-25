.PHONY: help install lint format test test_ui hooks clean # указываем утилите make, что цели это команды, а не имена файлов

# Справка
help:
	@echo ""
	@echo "Available commands:"
	@echo "  make install     - Установить зависимости"
	@echo "  make lint        - Проверить стиль кода (black, isort, flake8)"
	@echo "  make format      - Отформатировать код (black + isort)"
	@echo "  make test        - Запустить все pytest-тесты"
	@echo "  make test_ui     - Запустить UI-тесты (pytest -m ui)"
	@echo "  make hooks       - Установить и обновить pre-commit хуки"
	@echo "  make clean       - Очистить кеш и временные файлы"
	@echo ""

# Установить зависимости
install:
	pip install --upgrade pip
	pip install -r requirements.txt

# Проверка кода линтерами
lint:
	black --check .
	isort --check .
	flake8 .

# Форматирование кода линтерами
format:
	isort .
	black .

# Запуск тестов
test:
	pytest

# Запуск тестов по тегу @pytest.mark
test_ui:
	pytest -m ui

# Установка и обновление pre-commit
hooks:
	pre-commit install
	pre-commit autoupdate

# Очистить кэш
clean:
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type d -name ".pytest_cache" -exec rm -rf {} +
	@rm -rf .coverage htmlcov
	@echo "Clean complete"