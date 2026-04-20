import json as json_lib

from format.regex import formatRegex, formatRegexRetrie
from format.yaml import formatYaml

def formatOutput(format, resultList, package, pathOutput, givevariations=False, betterRegex=False):
    """
    Call different function to create the right format file
    """

    # Sanitize package name for use as filename (replace / and @ for npm scoped packages)
    safe_name = package.replace("/", "__").replace("@", "").replace("\\", "_")

    if format == "text":
        if pathOutput and not pathOutput == "-":
            with open(f"{pathOutput}/{safe_name}.txt", "w", encoding='utf-8') as write_file:
                for element in resultList:
                    if givevariations:
                        write_file.write(f"{element[0]}, {element[1]}\n")
                    else:
                        write_file.write(element + "\n")
        elif pathOutput == "-":
            for element in resultList:
                if givevariations:
                    print(f"{element[0]}, {element[1]}")
                else:
                    print(element)

    elif format == "json":
        if givevariations:
            output = {"package": package, "variations": [{"name": e[0], "algorithm": e[1]} for e in resultList]}
        else:
            output = {"package": package, "variations": resultList}

        if pathOutput and not pathOutput == "-":
            with open(f"{pathOutput}/{safe_name}.json", "w", encoding='utf-8') as write_file:
                json_lib.dump(output, write_file, indent=2, ensure_ascii=False)
        elif pathOutput == "-":
            print(json_lib.dumps(output, indent=2, ensure_ascii=False))

    elif format == "regex":
        if betterRegex:
            regex = formatRegexRetrie(resultList, givevariations)
        else:
            regex = formatRegex(resultList, givevariations)
        if pathOutput and not pathOutput == "-":
            with open(f"{pathOutput}/{safe_name}.regex", "w", encoding='utf-8') as write_file:
                write_file.write(regex)
        elif pathOutput == "-":
            print(regex)

    elif format == "yaml":
        yaml_file = formatYaml(resultList, package, givevariations)
        if pathOutput and not pathOutput == "-":
            import yaml
            with open(f"{pathOutput}/{safe_name}.yml", "w", encoding='utf-8') as write_file:
                yaml.dump(yaml_file, write_file)
        elif pathOutput == "-":
            print(yaml_file)
    else:
        print(f"Unknown format: {format}. Will use text format instead")
        formatOutput("text", resultList, package, pathOutput, givevariations)