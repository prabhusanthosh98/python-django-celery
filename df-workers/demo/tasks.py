from celery import shared_task
import time
from appdynamics.agent import api as appd
appd_env = {
    'APPD_CONFIG_FILE': '/root/appdynamics-test.cfg'
}




@shared_task
def test2():
    pass



@shared_task
def execute_long_work(model):
    appd.init(appd_env, 100000)

    mybt = appd.start_bt('/test_py')

    print('Starting long execution')

    time.sleep(5)
    print('almost there')

    time.sleep(5)

    test2.delay()
    print('Done')
    
    appd.end_bt(mybt)
    appd.shutdown()
    


