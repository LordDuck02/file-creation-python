def main():
    print("Welcome to duck stuff")
    choose = input("[1] - Create file \n[2] - PLACEHOLDER \n: ")
    if choose == '1':
        filename = input('Type the file name: ')
        destination = input('Type the destination: ')
        content = input('Type the content of the file: ')
        try:
            if os.path.exists(destination):
                print(f'{filename} created in {destination}')
                with open(filename, 'w') as file:
                    file.write(content)
                shutil.move(filename, destination)
            else:
                print('Couldnt find destination.')
        except FileNotFoundError:
            print(f'Couldnt find file.')
    elif choose == '2':
        print('no.')
