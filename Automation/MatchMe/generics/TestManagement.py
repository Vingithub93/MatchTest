import dotenv, os, Conf_Reader
import testrail

def get_testrail_client():
    "Get the TestRail account credentials from the testrail.env file"
    testrail_file = os.path.join(os.path.dirname(__file__),'testrail.env')
    #Get the TestRail Url
    testrail_url = Conf_Reader.get_value(testrail_file,'TESTRAIL_URL')
    print testrail_url
    client = testrail.APIClient(testrail_url)
    #Get and set the TestRail User and Password
    client.user = Conf_Reader.get_value(testrail_file,'TESTRAIL_USER')
    client.password = Conf_Reader.get_value(testrail_file,'TESTRAIL_PASSWORD')
    return client

def update_testrail(case_id,run_id,result_flag,msg=""):
    "Update TestRail for a given run_id and case_id"
    update_flag = False
    #Get the TestRail client account details
    client = get_testrail_client()
 
    #Update the result in TestRail using send_post function. 
    #Parameters for add_result_for_case is the combination of runid and case id. 
    #status_id is 1 for Passed, 2 For Blocked, 4 for Retest and 5 for Failed
    status_id = 1 if result_flag is True else 5
 
    if run_id is not None:
        try:
            result = client.send_post(
                'add_result_for_case/%s/%s'%(run_id,case_id),
                {'status_id': status_id, 'comment': msg })
        except Exception,e:
            print 'Exception in update_testrail() updating TestRail.'
            print 'PYTHON SAYS: '
            print e
        else:
            print 'Updated test result for case: %s in test run: %s with msg:%s'%(case_id,run_id,msg)
 
    return update_flag

def get_project_id(project_name):
        "Get the project ID using project name"
        client = get_testrail_client()
        project_id=None
        projects = client.send_get('get_projects')
        for project in projects:
            if project['name'] == project_name: 
                project_id = project['id']
                #project_found_flag=True
                break
        print project_id
        return project_id
 
def get_run_id(test_run_name,project_name):
        "Get the run ID using test name and project name"
        run_id=None
        client = get_testrail_client()
        project_id = get_project_id(project_name)
        try:
            test_runs = client.send_get('get_runs/%s'%(project_id))
        except Exception,e:
            print 'Exception in update_testrail() updating TestRail.'
            print 'PYTHON SAYS: '
            print e
            return None
        else:
            for test_run in test_runs:
                if test_run['name'] == test_run_name:
                    run_id = test_run['id']
                    break
            return run_id

get_project_id('Second')
get_run_id('Second_Test', 'Second')
update_testrail('2', '1', True, 'Test case is passed of Second project')