import os

output_file = 'result.txt'

def merge_files(output_file):
    """
    Объединяет содержимое всех текстовых файлов в текущей директории в один файл,
    отсортировав их по количеству строк.
    """
    files_data = []

    # Считываем содержимое всех текстовых файлов
    for file_name in os.listdir():
        if file_name.endswith('.txt') and file_name != output_file:  # Исключаем результирующий файл
            with open(file_name, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                files_data.append({
                    'name': file_name,
                    'line_count': len(lines),
                    'content': lines
                })

    # Сортируем файлы по количеству строк
    files_data.sort(key=lambda x: x['line_count'])

    # Создаем результирующий файл
    with open(output_file, 'w', encoding='utf-8') as output:
        for file_data in files_data:
            # Записываем служебную информацию
            output.write(f"{file_data['name']}\n")
            output.write(f"{file_data['line_count']}\n")
            # Записываем содержимое файла
            output.writelines(file_data['content'])
            output.write('\n')  # Разделяем файлы пустой строкой



# Пример использования
if __name__ == "__main__":
    output_file = 'result.txt'  # Имя результирующего файла
    merge_files(output_file)