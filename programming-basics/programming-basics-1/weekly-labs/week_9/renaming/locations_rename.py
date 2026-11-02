"""
This module provides functions for reading from a formatted text file and writing
the extracted data to a CSV file. It specifically processes geographic data,
modifying place names based on certain rules and generating structured information
about regions, administrative areas, and old/new names.

Functions:
    read_file(filename: str) -> dict:
        Reads a formatted text file and extracts geographic data, applying specific
        transformations to place names. Returns a dictionary with tuples containing
        region name, administrative area, and old place name as keys, and the new
        name as values.

    write_file(dct: dict, filename: str) -> None:
        Writes a dictionary of geographic data to a CSV file, using specified column
        headers for region name, administrative area, old place name, and new place
        name.
"""


def read_file(filename: str) -> dict:
    """
    Reads a specified file to map old names to new names within administrative divisions.

    The file should contain formatted lines specifying name changes for different areas.
    This function parses that information and returns a dictionary with old names as keys
    and new names as values.

    Example:
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode='w+', suffix=".txt", encoding='utf-8') as temp_input:
    ...     _ = temp_input.write('Про перейменування окремих населених пунктів та районів\\n'
    ...                          '1. Перейменувати такі населені пункти та райони:\\n'
    ...                          '1) у Вінницькій області:\\n'
    ...                          'село Червоне Барського району на село Грабівці;\\n'
    ...                          'село Красне Вінницького району на село Махнівка;\\n'
    ...                          '3) у Дніпропетровській області:\\n'
    ...                          'місто Дніпродзержинськ на місто Кам’янське;\\n'
    ...                          'Дніпропетровський район на Дніпровський район;\\n'
    ...                          '2. Ця Постанова набирає чинності.')
    ...     _ = temp_input.seek(0)
    ...     read_file(temp_input.name)
    {('Вінницька область', 'Барський район', 'с.Червоне'): 'с.Грабівці', \
('Вінницька область', 'Вінницький район', 'с.Красне'): 'с.Махнівка', \
('Дніпропетровська область', '', 'м.Дніпродзержинськ'): 'м.Кам’янське', \
('Дніпропетровська область', '', 'Дніпропетровський район'): 'Дніпровський район'}
    """
    with open(filename, "r", encoding="utf-8") as file:
        result = {}
        oldname = ""
        adm_region = ""
        region = ""
        for line in file:
            line = line.strip().strip(";").strip(":").strip(".")
            if line.startswith("2."):
                break
            if " на " not in line:
                if "області" in line:
                    region = line.split(" ")[2][:-2] + "а область"
                continue
            line = line.replace("селище міського типу", "смт")
            line = line.replace("селище ", "с-ще ")
            line = line.replace("село ", "с.")
            line = line.replace("місто ", "м.")
            newline = line.split(" на ")
            temp = newline[0].split(" ")
            if line.count("район") == 2:
                oldname = newline[0]
                adm_region = ""
            elif "с.Жовтневе Новобузької міської ради Новобузького району" in line:
                adm_region = "Новобузький район"
                oldname = "с.Жовтневе Новобузької міської ради"
            elif "міської ради" in newline[0]:
                adm_region = temp[-3][:-2] + "а міська рада"
                oldname = " ".join(temp[:-3])
            elif "району" in newline[0]:
                adm_region = temp[-2][:-3] + "ий район"
                oldname = " ".join(temp[:-2])
            elif "району" not in line or "ради" not in line:
                adm_region = ""
                oldname = temp[0]
            result[(region, adm_region, oldname)] = newline[1]
        return result


def write_csv_file(dct: dict, filename: str) -> None:
    """
    Writes the processed geographic data from a dictionary to a CSV file. Each
    dictionary entry contains region name, administrative area, old place name, and
    new place name, which are written as rows in the output file.

    :param dct: A dictionary containing tuples (region, administrative area, old
                name) as keys and new place names as values.
    :param filename: The name of the file to write to.
    :return: None. This function only writes data to a file.

    Example:
    >>> data = {('Вінницька область', 'Барський район', 'c.Червоне'): 'c.Грабівці', \
('Вінницька область', 'Вінницький район', 'c.Красне'): 'c.Махнівка', \
('Вінницька область', 'Жмеринський район', 'c.Ленінка'): 'c.Варжинка', \
('Вінницька область', 'Жмеринський район', 'c.Чапаєвка'): 'c.Малі Коростівці', \
('Вінницька область', 'Крижопільський район', 'c.Радянське'): 'c.Княжа Криниця', \
('Вінницька область', 'Літинський район', 'c.Радянське'): 'c.Літинські Хутори'}
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode='w+', encoding='utf-8') as tmpfile:
    ...     _ = write_csv_file(data, tmpfile.name)
    ...     tmpfile.seek(0)
    ...     print(tmpfile.read())
    0
    regionname,areaname,oldname,newname
    Вінницька область,Барський район,c.Червоне,c.Грабівці
    Вінницька область,Вінницький район,c.Красне,c.Махнівка
    Вінницька область,Жмеринський район,c.Ленінка,c.Варжинка
    Вінницька область,Жмеринський район,c.Чапаєвка,c.Малі Коростівці
    Вінницька область,Крижопільський район,c.Радянське,c.Княжа Криниця
    Вінницька область,Літинський район,c.Радянське,c.Літинські Хутори
    <BLANKLINE>
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write("regionname,areaname,oldname,newname\n")
        for data, newname in dct.items():
            file.write(f"{data[0]},{data[1]},{data[2]},{newname}\n")


if __name__ == "__main__":
    inname = "renamed_locations_24.txt"
    outname = "renamed.csv"
    write_csv_file(read_file(inname), outname)
