import datetime
import sublime, sublime_plugin
f=open("C:/Users/darsh/AppData/Roaming/Sublime Text 3/Packages/User/qqqtxt.txt","r") 
contents=f.read()
class TimestampCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    timestamp = "[%s]\t" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    self.view.insert(edit, self.view.sel()[0].begin(),"/**\n *      author: Darshan_Bhangale\n *      created: "+timestamp+"\n**/\n"+contents)

# f.close()
# "/**\n*\t\t\tauthor:  Darshan_Bhangale\n*\t\t\tcreated: +"timestamp"+\n       **/"
# "/**\n*\t\t\tauthor:  Darshan_Bhangale\n*\t\t\tcreated: +"timestamp"+\n       **/"