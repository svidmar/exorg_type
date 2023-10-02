# Project Title

Classify unclassified external organisations from Pure using ChatGPT's API

## Description

This script can be used to determine organisation type based on an organisations name, from a CSV file. Can be used to classify unclassified external organisations from Pure, using ChatGPT's API, and save the results in a CSV file (which can then be written back into Pure using Pure's API). Presented at Pure International Conference 2023. 

## Getting Started

### Dependencies

* Access to Pure
* API key for Open AI/Chat GPT
* csv library
* openai library


### Executing program

* Replace 'my_openai_apikey' with you actual API key
* Adjust prompt, so it matches the types of external organisations you have in your Pure (remember to change 'allowed_types' accordingly as well)
* Extract x number of external organisations from Pure with unknown type classification (include columns 'UUID' and organisation name as 'Name') - save as 'input.csv'  
* Run the script
* Output will be saved as 'output.csv' in the same folder
* Evaluate results and write new type classification back to Pure using Pure's API 
```
```


## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the [GNU General Public License v3.0] License - see the LICENSE.md file for details
