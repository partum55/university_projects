def process_file_with_generator(input_file, output_file, key="friendship"):
    def line_generator(file_path, key):
        """Генератор, який обробляє файл построково."""
        in_main_section = False
        with open(file_path, "r", encoding="iso-8859-1") as file:
            for line in file:
                if not in_main_section:
                    yield line  # Зберігаємо початок файлу
                    if "\t" in line.strip() or "http://" in line.strip():  # Основна частина починається після числа
                        in_main_section = True
                else:
                    if key in line:  # Віддаємо рядки, що містять ключ
                        yield line

    # Запис результату в новий файл
    with open(output_file, "w", encoding="utf-8") as dst:
        dst.writelines(line_generator(input_file, key))


# Виклик функції
input_file = "keywords.list"  # Задайте шлях до вашого файлу
output_file = "keywords_output.list"  # Задайте шлях до нового файлу
process_file_with_generator(input_file, output_file)
