
class Project:
    def __init__(self, project_num, project_nm, projectmanager_nm, status="Incomplete"):
        # creating constraints
        assert status in {"Complete", "Incomplete"}

        # initialising Project
        self.project_num=project_num
        self.project_nm = project_nm
        self.pm_nm = projectmanager_nm
        self.status = status


class Resources(Project):
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

class Task(Project):
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


def create_new_project():
    global pm
    global pn
    global pnum
    global sys_pn
    pn = input("Enter project name")
    pm = input("Enter project manager's name")
    pnum = input("Enter project number")
    sys_pn = f"{pn}_{pnum}"
    sys_pn = Project(pnum, pn, pm)


def add_resource():
    global  sys_rs_nm
    pn = input("Which project should the resource be allocated to")
    prn = input("Enter resource name")
    sys_rs_num = input("enter id number of resource")
    prba = input("how much money are you allocating to said resource")
    sys_rs_nm = f"{prn}_{sys_rs_num}"
    sys_rs_nm = Resources(pnum, pn, pm, prn, project_resource_budget_alloc=prba)


def add_tasks():
    global sys_tk_nm
    pn = input("enter project name")
    ptn = input("Enter task name")
    tk_num = input("enter task number")
    sys_tk_nm = f"{ptn}_{tk_num}"
    subtask_input = input("if you'll like to add subtask type (Y) else press enter")
    if not subtask_input == "Y":
        sys_tk_nm = Task(pnum, pn, pm, ptn)
    else:
        def add_subtasks():
            ptsn = input("enter subtask name")
            ptst = input("enter time allocated to subtask in minutes")
            return ptst, ptsn
        pt, ps = add_subtasks()
        sys_tk_nm = Task(pnum, pn, pm, ptn,subtask_nm=pt, subtask_tm_alloc=int(ps))






## action = input("will you like to save(s),retrieve(r),or edit(e)").upper()

# if action == "S":
 #   save()
# elif action == "R":
 #   retrieve()
# elif action == "E":
 #   print("coming soon")
# else:
 #    print("choose an option")

print("***************************Al pro***********************")
print("Create new project(N)")
print("Exit(E)")
user_action1 = input("Enter your choice(N or E)")
if user_action1 in {"N","E"}:
    if user_action1 == "N":
        create_new_project()
    elif user_action1 == "E":
        exit()
else:
    print("choose either new project(N) or exit(E)")

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