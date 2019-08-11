import splunk.admin as admin
import splunk.entity as en

class ConfigApp(admin.MConfigHandler):
  '''
  Set up supported arguments
  '''
  def setup(self):
    if self.requestedAction == admin.ACTION_EDIT:
      for arg in ['repository', 'folder']:
        self.supportedArgs.addOptArg(arg)
        
  '''
  Read the initial values of the parameters from the custom file
      myappsetup.conf, and write them to the setup page. 

  If the app has never been set up,
      uses .../app_name/default/myappsetup.conf. 

  If app has been set up, looks at 
      .../local/myappsetup.conf first, then looks at 
  .../default/myappsetup.conf only if there is no value for a field in
      .../local/myappsetup.conf

  For boolean fields, may need to switch the true/false setting.

  For text fields, if the conf file says None, set to the empty string.
  '''

  def handleList(self, confInfo):
    confDict = self.readConf("settings")
    if None != confDict:
      for stanza, settings in confDict.items():
        for key, val in settings.items():
          if key in ['repository'] and val in [None, '']:
            val = ''
          if key in ['folder'] and val in [None, '']:
            val = ''
          confInfo[stanza].append(key, val)
          
  '''
  After user clicks Save on setup page, take updated parameters,
  normalize them, and save them somewhere
  '''
  def handleEdit(self, confInfo):
    name = self.callerArgs.id
    args = self.callerArgs
    
    if self.callerArgs.data['repository'][0] in [None, '']:
      self.callerArgs.data['repository'][0] = ''  

    if self.callerArgs.data['folder'][0] in [None, '']:
      self.callerArgs.data['folder'][0] = ''  

        
    '''
    Since we are using a conf file to store parameters, 
write them to the [setupentity] stanza
    in app_name/local/myappsetup.conf  
    '''
        
    self.writeConf('settings', 'settings', self.callerArgs.data)
      
# initialize the handler
admin.init(ConfigApp, admin.CONTEXT_NONE)



