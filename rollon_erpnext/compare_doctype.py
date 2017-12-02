import frappe, json, git
from git import Repo

def input_string_for_data(branch, filepath):
	return "{0}:{1}".format(branch, filepath)

def dict_compare(d1, d2):
    d1_keys = set(d1.keys())
    d2_keys = set(d2.keys())
    intersect_keys = d1_keys.intersection(d2_keys)
    added = d1_keys - d2_keys
    removed = d2_keys - d1_keys
    modified = {o : (d1[o], d2[o]) for o in intersect_keys if d1[o] != d2[o]}
    same = set(o for o in intersect_keys if d1[o] == d2[o])
    return added, removed, modified, same

def compare_doctypes():
	original_branch = "v6.27.9"
	modified_branch = "master-mod"

	#Init repo
	repo = Repo("~/frappe-bench/apps/erpnext/")
	repo_git = repo.git

	f = open('/home/harsh/Desktop/files_to_compare.txt', 'rb')

	files = f.readlines()

	for filename in files:
		original_content = None
		modified_content = None
		try:
			original_content = repo_git.get_object_data(
				input_string_for_data(original_branch, filename)
			)
			original_content = json.loads(original_content)
			original_content = original_content[3]
		except Exception as e:
			print ("ORIGINAL: ", e.message)
		
		try:
			modified_content = repo_git.get_object_data(
				input_string_for_data(modified_branch, filename)
			)
			modified_content = json.loads(modified_content)		 	
			modified_content = modified_content[3]	
		except Exception as e:
			print ("MODIFIED: ", e.message)

		
		if type(modified_content[3]) == dict and type(original_content[3]) == dict:
			added, removed, modified, same = dict_compare(original_content, modified_content)

			print("AMRS", added, removed, modified, same)
