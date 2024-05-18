def create_new_project():
    pn = input("Enter project name")
    pm = input("Enter project manager's name")


def add_resource():
    pn = input("Which project should the resource be allocated to")
    prn = input("Enter resource name")
    prba = input("how much money are you allocating to said resource")


def add_tasks():
    pn = input("enter project name")
    ptn = input("Enter task name")


def add_subtasks():
    pn = input("enter project name")
    ptsn = input("enter subtask name")
    ptst = input("enter time allocated to subtask in minutes")


class Project:
    def __init__(self, project_nm, projectmanager_nm, status="Incomplete"):
        # creating constraints
        assert status in {"Complete", "Incomplete"}

        # initialising Project
        self.project_nm = project_nm
        self.pm_nm = projectmanager_nm
        self.status = status


class Resources(Project):
    def __init__(self, project_nm, projectmanager_nm, status="Incomplete", resources_nm=None, resources_status=None,
                 budget_allocation=0.00):
        # creating constraints
        assert resources_status in {"obtained", "none", "some"}
        assert budget_allocation >= 0.00

        # initialising Project
        super().__init__(project_nm, projectmanager_nm, status)
        self.rs = resources_nm
        self.rs_stat = resources_status
        self.budget = budget_allocation

class Task(Project):
    def __init__(self, project_nm, projectmanager_nm, status="Incomplete", task_nm=None, task_status=None,
                 subtask_nm=None, subtask_status=None, subtask_tm_alloc=0):
        # creating constraints
        assert task_status in {"Complete", "Incomplete", "None"}
        assert subtask_status in {"Complete", "Incomplete", "None"}
        assert subtask_tm_alloc >= 0

        # initialising Project
        super().__init__(project_nm, projectmanager_nm, status)
        self.tk_nm = task_nm
        self.tk_stat = task_status,m
        self.sk_nm = subtask_nm
        self.sk_stat = subtask_status
        self.sk_tm = subtask_tm_alloc


project1 = Project("mk_project_manager", "Albert", "Incomplete")

resource1 = Resources("projectTrial", "albert", "Incomplete",
                      "laptop", "some", 10)

task1 = Task("projectTrial", "albert", "Incomplete", "allow saving",
             "Complete", "import/export cms", "Incomplete", 30)


task1.status = "Complete"

project_name = project1.project_nm
project_manager = project1.pm_nm
project_status = project1.status
project_resource_name = resource1.rs
project_resource_status = resource1.rs_stat
project_resource_budget_alloc = resource1.budget
project_task_name = task1.tk_nm
project_task_status = task1.tk_stat
project_task_subtask_name = task1.sk_nm
project_task_subtask_status = task1.sk_stat
project_task_subtask_time = task1.sk_tm

sv_items = (f"project name({project_name}) : \t\t project manager({project_manager}) \t\t project status = {project_status}"
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


action = input("will you like to save(s),retrieve(r),or edit(e)").upper()

if action == "S":
    save()
elif action == "R":
    retrieve()
elif action == "E":
    print("coming soon")
else:
    print("choose an option")


