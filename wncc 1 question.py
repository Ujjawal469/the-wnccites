def is_skill_met(skill, required_level, participant_skills):
    return participant_skills[skill] >= required_level

def is_co_mentor_available(project_name, participant, participants, projects):
    for role in projects[project_name]:
        if participant != role['participant'] and role['participant'] in participants:
            if is_skill_met(role['skill'], role['required_level'] - 1, participants[role['participant']]):
                return True
    return False

N = int(input())
participants = {}
for _ in range(N):
    roll_number, *skills = input().split()
    skills = [0] + list(map(int, skills))  # Append 0 at the beginning of skills
    participants[roll_number] = skills

M = int(input())
projects = {}
for _ in range(M):
    project_name, *roles = input().split()
    roles = [{'participant': -1, 'skill': i + 1, 'required_level': int(level)} for i, level in enumerate(roles)]
    projects[project_name] = roles

completed_projects = 0
for project_name, roles in projects.items():
    is_project_completed = True
    for role in roles:
        for participant, skills in participants.items():
            if is_skill_met(role['skill'], role['required_level'], skills):
                role['participant'] = participant
                break
            elif is_skill_met(role['skill'], role['required_level'] - 1, skills):
                if is_co_mentor_available(project_name, participant, participants, projects):
                    role['participant'] = participant
                    break
        if role['participant'] == -1:
            is_project_completed = False
            break
    if is_project_completed:
        completed_projects += 1

print(completed_projects)
