with open("hr_system.txt", "r") as file:
    for line in file:
        line = line.strip()
        
        parts = line.split()
        
        name = parts[0]
        id_number = parts[1]
        job_title = parts[2]
        salary = float(parts[3])
        
        paycheck_amount = salary / 24.0
        
        if job_title == "Engineer":
            paycheck_amount += 1000
        
        print(f"{name} (ID: {id_number}), {job_title} - ${paycheck_amount:.2f}")