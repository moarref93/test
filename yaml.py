from yaml import load

def parse(file_name):  
    try:    
        with open(file_name, 'r') as file:  
            data = load(file)
        
        for key, value in data.items():  
            print(f"{key} is : and {value} is :") 

    except FileNotFoundError:
        print("The specified file does not exist.")

yaml_file_path = 'data.yaml'  

parse(yaml_file_path)  
