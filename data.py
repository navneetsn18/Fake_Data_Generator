import names,random
from geopy.geocoders import Nominatim
from faker import Faker
from tqdm import tqdm
import pandas as pd
import json

fake = Faker() 

def generate_mobile_number():
    return random.randint(7011312412,9996859785)

def genrate_name(email):
    name = email.split("@")[0]
    if "." in name:
        return [name.split(".")[0].capitalize(),name.split(".")[1].capitalize()]
    else:
        return [name.capitalize(),str(names.get_last_name()).capitalize()]

def generate_address():
    address = fake.address()
    geolocator = Nominatim(user_agent="geoapiExercises")
    part1 = address.split(",")[0]
    part2 = address.split(",")[1]
    addr = str(geolocator.geocode(part2.split(" ")[1]))
    if addr.split(",")[1]:
        address = {
            "line1":part1.split("\n")[0],
            "line2":part1.split("\n")[1],
            "city":part2.split(" ")[1],
            "state":addr.split(",")[0],
            "country":str(addr.split(",")[1]).strip(),
            "zip":part2.split(" ")[2]
        }
    return address

def generate_job():
    jobs=["Developer",
          "Engineer",
          "Architect",
          "Analyst",
          "Business Analyst",
          "Business Development",
          "Business Manager",
          "SDE",
          "Software Engineer",
          "Software Developer",
          "Software Architect",
          "Software Developer",
          "Software Tester",
          "Programmer Analyst Trainee",
          "Programmer Analyst",
          "Programmer",
          "Programmer Trainee",
          "Associate",
          "Associate Trainee",
          "Associate Developer",
          "Associate Developer Trainee",
          "Associate Software Engineer",
          "Associate Software Engineer Trainee",
          "Tech Lead",
          "Tech Lead Trainee",
          "Tech Lead Developer",
          "Tech Lead Developer Trainee",
          "Tech Lead Software Engineer",
          "Tech Lead Software Engineer Trainee",
          "Senior Software Engineer",
          "Senior Software Engineer Trainee",
          "Lead Engineer",
          "Lead Engineer Trainee",
          "HR",
          "HR Trainee",
          "HR Manager",
          "HR Manager Trainee",
          "HR Manager Developer",
          "Python Developer",
          "Python Developer Trainee",
          "Java Developer",
          "Java Developer Trainee",
          "Java Developer",
          "Java Developer Trainee",
          "Full stack Developer",
          "Full stack Developer Trainee",
          "Full Stack Engineer",
          "Front End Developer",
          "Front End Developer Trainee",
          "Front End Engineer",
          "UI Developer",
          "UI Developer Trainee",
          "UI/UX Designer",
          "UI/UX Designer Trainee",
          "UX Designer",
          "Manager Projects"
    ]
    return random.choice(jobs)

if __name__ == "__main__":
    df = pd.read_csv('data.csv')
    data = {}
    x=0
    print("Generating Data...")
    for i in tqdm(df.index):
        addr = None
        while addr is None:
            try:
                addr = generate_address()
                if addr["country"] != "United States":
                    addr = generate_address()
                    if addr["country"] != "United States":
                        addr = generate_address()
                        if addr["country"] != "United States":
                            addr = generate_address()
            except:
                pass
        data[x]={}
        data[x]["name"] = genrate_name(df["Email"][i])
        data[x]["email"] = df["Email"][i]
        data[x]["address"] = addr
        data[x]["mobile"] = generate_mobile_number()
        data[x]["company"] = df["Email"][i].split("@")[1].split(".")[0]
        data[x]["job"] = generate_job()
        x+=1
    with open("data.json", "w") as file:
        json.dump(data, file)
    print("Data Generated Successfully!!!")