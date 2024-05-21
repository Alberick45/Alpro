# Dictionary for projects and the corresponding manager
Projects = {}
# lists of project names only
Eprojects = []


def save_project(x):  # save project name,number and manager in projects.txt
    x = x.capitalize()
    with open("Project.txt", "a") as f:
        f.write(x)


def retrieve_project_list():  # retrieve project name,number and manager from projects.txt
    global Projects, Eprojects
    Projects = {}
    Eprojects = []

    try:
        with open("Project.txt", "r") as f:
            reader = f.read().strip()
            if reader == "":
                Projects = {}
            else:
                pairs = reader.split(",")
                for pair in pairs:
                    print(pair)  # Debug print statement
                    if ':' in pair:
                        keys, values = pair.split(':', 1)  # Split only on the first colon
                        keys = keys.strip().capitalize()
                        values = values.strip().capitalize()
                        values = values.split('+')
                        values = [v.strip() for v in values]  # Strip each value
                        Projects[keys] = values  # store as  dictionary in Projects
                        id = values[0]
                        Eprojects.append(id)  # store project name as list in Eprojects
    except FileNotFoundError:
        with open("Project.txt", "w") as f:
            f.write("")
        print("No projects found.")
        Projects = {}
        Eprojects = []


class Project:  # main class where projects objects are uniquely created
    def __init__(self, project_num, project_nm, projectmanager_nm, status="Incomplete"):
        # creating constraints
        assert status in {"Complete", "Incomplete"}

        # initialising Project
        self.project_num=project_num
        self.project_nm = project_nm
        self.pm_nm = projectmanager_nm
        self.status = status


class Resources(Project):  # subclass where resource objects are uniquely differentiated under each unique project
    def __init__(self, project_num, project_nm, projectmanager_nm, status="Incomplete", resources_nm=None, resources_status=None,
                 budget_allocation=0.00):
        # creating constraints
        assert resources_status in {"obtained", "none", "some"}
        assert budget_allocation >= 0.00

        # initialising Project
        super().__init__(project_num, project_nm, projectmanager_nm, status)
        self.rs = resources_nm
        self.rs_stat = resources_status
        self.budget = budget_allocation


class Task(Project):  # subclass where Tasks  are uniquely differentiated under each unique project
    def __init__(self, project_num, project_nm, projectmanager_nm, status="Incomplete", task_nm=None, task_status=None,
                 subtask_nm=None, subtask_status=None, subtask_tm_alloc=0):
        # creating constraints
        assert task_status in {"Complete", "Incomplete", "None"}
        assert subtask_status in {"Complete", "Incomplete", "None"}
        assert subtask_tm_alloc >= 0

        # initialising Project
        super().__init__(project_num, project_nm, projectmanager_nm, status)
        self.tk_nm = task_nm
        self.tk_stat = task_status
        self.sk_nm = subtask_nm
        self.sk_stat = subtask_status
        self.sk_tm = subtask_tm_alloc


def create_new_project():  # create new project object
    global pm
    global pn
    global pnum
    global sys_pn
    print("\n\n************************* New Project ***********************")
    pn = input("Enter project name").capitalize()
    pm = input("Enter project manager's name").capitalize()
    pnum = input("Enter project number").capitalize()
    sys_pn = f"{pn}_{pnum}".capitalize()
    sys_pn = Project(pnum, pn, pm)
    Projects[pnum] = [pn, pm]
    save_project(f"{pnum} : {pn} + {pm},\n")
    print(f"Creating project {pn} \n")
    edit_project(pn)


def edit_project(name_of_project):  # edit existing project object
    print(f"\n\n**********************  Editing {name_of_project}  *********************\n")
    print("edit project's name or manager's name (1)\n")
    print("Update project status (2)\n")
    print("update team members (3)\n")
    print("update resources (4)\n")
    print("update tasks (5)\n")
    print("Exit to home(6)\n")

    euserinput = int(input("what will you like to do"))
    if not euserinput in [1,2,3,4,5,6]:
        print("enter a number that corresponds with one of the following")
        home()
    else:
        if euserinput == 1:
            # add edit project name /manager name function
            print("coming soon")
        elif euserinput == 2:
            # add update project status function
            print("coming soon")
        elif euserinput == 3:
            # add team members add function
            print("coming soon")
        elif euserinput == 4:
            # add_resource(name_of_project)
            print("updates underway")
        elif euserinput == 5:
            # add_tasks(name_of_project)
            print("updates underway")
        elif euserinput == 6:
            pass

    print("Exiting to home screen")
    home()


def add_resource(project_name):  # edit existing project object by editing resource
    print(f"\n\n**********************  Resources for {project_name}  *********************\n")
    global sys_rs_nm
    pn = project_name
    prn = input("Enter resource name").capitalize()
    sys_rs_num = input("enter id number of resource")
    prba = float(input("how much money are you allocating to said resource"))
    sys_rs_nm = f"{prn}_{sys_rs_num}"
    sys_rs_nm = Resources(pnum, pn, pm, prn, project_resource_budget_alloc=prba)


def add_tasks(project_name):  # edit existing project object by editing tasks
    print(f"\n\n**********************  Tasks under {project_name}  *********************\n")
    global sys_tk_nm
    pn = project_name
    ptn = input("Enter task name").capitalize()
    tk_num = input("enter task number")
    sys_tk_nm = f"{ptn}_{tk_num}"
    subtask_input = input("if you'll like to add subtask type (Y) else press enter").capitalize()
    if not subtask_input == "Y":
        sys_tk_nm = Task(pnum, pn, pm, ptn)
    else:
        def add_subtasks():  # edit existing project object by editing subtasks
            ptsn = input("enter subtask name").capitalize()
            ptst = input("enter time allocated to subtask in minutes").capitalize()
            return ptst, ptsn
        pt, ps = add_subtasks()
        sys_tk_nm = Task(pnum, pn, pm, ptn,subtask_nm=pt, subtask_tm_alloc=int(ps))


def home():  # index page
    print("\n\n*************************** Al pro ***********************")

    print("***************************  Home  ***********************")

    def home_question():
        print("Create new project(N)")
        print("Delete existing project(D)")
        print("Exit(E)")
        if not Projects:
            user_action1 = input("Enter your choice(N,D or E)")
        else:
            print("edit existing(M)")
            user_action1 = input("Enter your choice(N,D,E or M)")
        return user_action1.capitalize()

    user_answer = home_question()
    print(user_answer)
    if user_answer in {"N", "D", "E", "M"}:
        if user_answer == "N":
            create_new_project()
        elif user_answer == "D":
            udel = input("which project will you like to delete").capitalize()
            """if udel in Eprojects:          (#  not working so well)
                print(udel)
                del (Projects[udel])
            else:
                print(f"{udel} is not a project")"""
            home()
        elif user_answer == "E":
            exit()
        elif user_answer == "M":
            print(Eprojects)
            up_nm = input("Enter name of project").capitalize()
            if Projects:
                if up_nm in Eprojects:
                    edit_project(up_nm)
                else:
                    print(up_nm)
                    print("not existing will you like to create a new project")
                    home()
            else:
                print("no project yet"
                      ", will you like to create one?")
                home()
    else:
        print("choose either new project(N) or exit(E) or edit(M)")
        home()

"""
project_name = sys_pn.project_nm
project_num = sys_pn.project_num
project_manager = sys_pn.pm_nm
project_status = sys_pn.status
project_resource_name = sys_rs_nm.rs
project_resource_status = sys_rs_nm.rs_stat
project_resource_budget_alloc = sys_rs_nm.budget
project_task_name = sys_tk_nm.tk_nm
project_task_status = sys_tk_nm.tk_stat
project_task_subtask_name = sys_tk_nm.sk_nm
project_task_subtask_status = sys_tk_nm.sk_stat
project_task_subtask_time = sys_tk_nm.sk_tm

sv_items = (f"project_num({project_num}), project name({project_name}) : \t\t project manager({project_manager}) \t\t project status = {project_status}"
            f" \n project resource name({project_resource_name})  \t\t project resource status = {project_resource_status}"
            f" \t\t project resource budget allocation = {project_resource_budget_alloc}  \n project task name({project_task_name})"
            f" \t\t project task status = {project_task_status}  \n\t\t project task subtask name({project_task_subtask_name}) \t\t project task subtask status = {project_task_subtask_status}"
            f" \t\t project task subtask time = {project_task_subtask_time} minutes \n\n\n")


def save():
    with open("alpro.txt", "a") as f:
        f.write(sv_items)
        f.close()


def retrieve():
    with open("alpro.txt", "r") as f:
        stored_message = f.read()
    print(stored_message)


"""

# note will have to separate others into modules to make it readable

# main code
retrieve_project_list()
home()
