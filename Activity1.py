def MathMajorsSet(): 
    infile = open("math.txt", "r")
    data = infile.readlines()
    infile.close()

    mathmajors = set()
    for line in data :
        line = line.strip()
        mathmajors.add(line)
    #print(mathmajors)
    return mathmajors
#MathMajorsSet()

def CSSet(): 
    infile = open("cs.txt", "r")
    data = infile.readlines()
    infile.close()

    csmajors = set()
    for line in data :
        line = line.strip()
        csmajors.add(line)
    #print(csmajors)
    return csmajors
#CSSet()

def CSandMathMajors():
    csmajors = CSSet()
    mathmajors = MathMajorsSet()
    csandmathmajors = csmajors.intersection(mathmajors)
    print(csandmathmajors)
    return csandmathmajors
CSandMathMajors()

def CSorMathMajors():
    csmajors = CSSet()
    mathmajors = MathMajorsSet()
    csormathmajors = csmajors.union(mathmajors)
    print(csormathmajors)
    return csormathmajors
CSorMathMajors()

def onlyCSMajors():
    csmajors = CSSet()
    mathmajors = MathMajorsSet()
    onlycsmajors = csmajors.difference(mathmajors)
    print(onlycsmajors)
    return onlycsmajors
onlyCSMajors()

def StudentsByYear(): 
    infile = open("studentYear.txt", "r")
    data = infile.readlines()
    infile.close()

    students_by_year = {}
    for line in data:
        line = line.strip()
        parts = line.split("\t")
        if len(parts) == 2:
            year, student = parts
            if year not in students_by_year:
                students_by_year[year] = set()
            students_by_year[year].add(student)
    
    # Create sets for each grade level
    freshman = students_by_year.get("1", set())
    sophomore = students_by_year.get("2", set())
    junior = students_by_year.get("3", set())
    senior = students_by_year.get("4", set())

    print("Freshman:", freshman)
    print("Sophomore:", sophomore)
    print("Junior:", junior)
    print("Senior:", senior)

    return freshman, sophomore, junior, senior

StudentsByYear()
def SophomoreCSMajors():
    csmajors = CSSet()
    sophomore = StudentsByYear()[1]
    sophomores = csmajors.intersection(sophomore)
    print(f"all the sophomores that are CS majors are {sophomores}")
    return sophomores
SophomoreCSMajors()

def freshmannotmathorcs():
    csmajors = CSSet()
    mathmajors = MathMajorsSet()
    freshman = StudentsByYear()[0]
    notmathorcs = freshman.difference(csmajors.union(mathmajors))
    print(f"all the freshman that are not math or cs majors are {notmathorcs}")
freshmannotmathorcs()

def SeniorCSorMath():
    csmajors = CSSet()
    mathmajors = MathMajorsSet()
    senior = StudentsByYear()[3]
    seniors = senior.intersection(csmajors.union(mathmajors))
    print(f"all the seniors that are CS or Math majors are {seniors}")
SeniorCSorMath()

