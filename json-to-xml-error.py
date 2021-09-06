
import xmltodict

student = {
    "name" : "Shubham",
    "marks" : {
        "math" : 92,
        "english" : 99
    },
    "id" : "s387hs3"
}

print(xmltodict.unparse(student, pretty=True))
