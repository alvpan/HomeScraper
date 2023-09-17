import re
import pprint
#needs merging and cleanup

def PriceExtractor(file_path):
    prices = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            #starts with EUR symbol and conrinues with a number, maybe a dot, and more numbers.
            pattern = r'€(\d.?\d+)'
            matches = re.findall(pattern, text)
            if matches:
                for match in matches:
                    print(f"Found €{match}")
                    #fill in the price list
                    prices.append(int(match.replace(".","")))              
            else:
                print("No match!")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"ERROR!: {str(e)}")
    print("NUMBERS:\n")
    print(prices)
    print("\nsize: ", len(prices))
    return(prices, len(prices))


def SizeExtractor(file_path):
    square_meters = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            pattern = r'\d+T|\d{2}7'
            matches = re.findall(pattern, text)
            if matches:
                for match in matches:
                    print(f"Found {match}T")
                    square_meters.append(int(match.replace("T","")))
            else:
                print("No matches found.")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    print("SQUARE METERS:\n")
    print(square_meters)
    print("\nsize: ",len(square_meters))
    return(square_meters,len(square_meters))

square_results = SizeExtractor("less_text.txt")
price_results = PriceExtractor("less_text.txt")

#DICTIONARIES/////////////////////////////////////////
def DictCreator(square_results,price_results):
    if(price_results[1]==square_results[1]):
        stat_dictionary = {key: [price_results[0][i] for i in range(len(square_results[0])) if square_results[0][i] == key] for key in square_results[0]}
        return(stat_dictionary)

result_dict = DictCreator(square_results, price_results)
pprint.pprint(result_dict)

 
def GetDictAverage(dictionary):
    average = []
    dict_values = list(dictionary.values())
    print("DICT VALUES:")
    print(dict_values) 
    for i in range(len(dict_values)):
        average.append(int(sum(dict_values[i])/len(dict_values[i])))
    print("AVERAGES:")
    print(average)

GetDictAverage(result_dict)