#!/usr/local/bin/python3
import cmd2
import subprocess
import os
black = "\u001b[30m"
red = "\u001b[31m"
green = "\u001b[32m"
yellow = "\u001b[33m"
blue = "\u001b[34m"
magenta = "\u001b[35m"
cyan = "\u001b[36m"
white = "\u001b[37m"
art_color = '\033[91m'
remaining_color = '\033[92m'
class FlutomateCommands(cmd2.Cmd):
    

    intro = "Welcome to the Flutter CLI. Type 'help' for a list of commands."
    prompt = red+"Flutomate> "+remaining_color


    def do_fcreate(self, arg):
        """Create Project"""
        try:
            foldername=input("Enter your app name: ")
            result=subprocess.run("flutter create "+foldername,shell=True, text=True,capture_output=True)
            self.poutput(cyan+result.stdout+remaining_color)
            subprocess.run(f"cd {foldername}",shell=True,capture_output=True, text=True)
            subprocess.run(f"code {foldername}",shell=True,capture_output=True, text=True)

        except subprocess.CalledProcessError as e:
            self.poutput(f"Error: {e}")
        except FileNotFoundError:
            self.poutput("Flutter not found. Make sure Flutter is installed and in your PATH.")
    

    def do_fanalyze(self, arg):
        """analyze Project"""
        try:
            result=subprocess.run("flutter analyze",shell=True, text=True,capture_output=True)
            self.poutput(cyan+result.stdout+remaining_color)
        except subprocess.CalledProcessError as e:
            self.poutput(f"Error: {e}")
        except FileNotFoundError:
            self.poutput("Flutter not found. Make sure Flutter is installed and in your PATH.")


    def do_ftest(self, arg):
        """test Project"""
        try:
            result=subprocess.run("flutter test",shell=True, capture_output=True, text=True)
            self.poutput(cyan+result.stdout+remaining_color)
        except subprocess.CalledProcessError as e:
            self.poutput(f"Error: {e}")
        except FileNotFoundError:
            self.poutput("Flutter not found. Make sure Flutter is installed and in your PATH.")
    
    def do_ftestcov(self, arg):
        """test coverage"""
        try:
            result=subprocess.run("flutter test --coverage",shell=True,capture_output=True, text=True)
            self.poutput(cyan+result.stdout+remaining_color)
            result1=subprocess.run("genhtml coverage/lcov.info -o coverage/html",shell=True,capture_output=True, text=True)
            self.poutput(cyan+result1.stdout+remaining_color)
            result2=subprocess.run("open coverage/html/index.html",shell=True,capture_output=True, text=True)
            self.poutput(cyan+result2.stdout+remaining_color)
        except subprocess.CalledProcessError as e:
            self.poutput(f"Error: {e}")
        except FileNotFoundError:
            self.poutput("Flutter not found. Make sure Flutter is installed and in your PATH.")

    def do_frun(self, arg):
        """run Project"""
        try:
            result=subprocess.run("flutter run lib/main.dart",shell=True,capture_output=True, text=True)
            self.poutput(cyan+result.stdout+remaining_color)
        except subprocess.CalledProcessError as e:
            self.poutput(f"Error: {e}")
        except FileNotFoundError:
            self.poutput("Flutter not found. Make sure you in right PATH.")

    def do_fver(self, arg):
        """check version"""
        try:
            result=subprocess.run("flutter --version",shell=True, capture_output=True, text=True)
            self.poutput(cyan+result.stdout+remaining_color)
        except subprocess.CalledProcessError as e:
            self.poutput(f"Error: {e}")
        except FileNotFoundError:
            self.poutput("Flutter not found. Make sure you in right PATH.")    
    
    def do_fpget(self, arg):
        """get packages"""
        try:
            result=subprocess.run("flutter pub get",shell=True, capture_output=True, text=True)
            self.poutput(cyan+result.stdout+remaining_color)
        except subprocess.CalledProcessError as e:
            self.poutput(f"Error: {e}")
        except FileNotFoundError:
            self.poutput("Flutter not found. Make sure you in right PATH.")
    def do_fclean(self, arg):
        """Clean Caches"""
        try:
            result=subprocess.run("flutter clean",shell=True,capture_output=True, text=True)
            self.poutput(cyan+result.stdout+remaining_color)
            result1=subprocess.run("flutter pub get",shell=True,capture_output=True, text=True)
            self.poutput(cyan+result1.stdout+remaining_color)
        except subprocess.CalledProcessError as e:
            self.poutput(f"Error: {e}")
        except FileNotFoundError:
            self.poutput("Flutter not found. Make sure you in right PATH.")
    def do_fbapk(self, arg):
        """build apk packages"""
        try:
            result=subprocess.run("flutter build apk --split-per-abi",shell=True,capture_output=True, text=True)
            self.poutput(result.stdout)
        except subprocess.CalledProcessError as e:
            self.poutput(f"Error: {e}")
        except FileNotFoundError:
            self.poutput("Flutter not found. Make sure you in right PATH.")
    def do_fbios(self, arg):
        """build ipa packages"""
        try:
            result=subprocess.run("fflutter build ios --debug --no-codesign",shell=True,capture_output=True, text=True)
            self.poutput(result.stdout)
        except subprocess.CalledProcessError as e:
            self.poutput(f"Error: {e}")
        except FileNotFoundError:
            self.poutput("Flutter not found. Make sure you in right PATH.")
    def do_fgenkey(self, arg):
        """build generate keystore  key"""
        try:
            result=subprocess.run("keytool -genkey -v -keystore ~/upload-keystore.jks -keyalg RSA \
          -keysize 2048 -validity 10000 -alias upload",shell=True, capture_output=True, text=True)
            self.poutput(result.stdout)
        except subprocess.CalledProcessError as e:
            self.poutput(f"Error: {e}")
        except FileNotFoundError:
            self.poutput("Flutter not found. Make sure you in right PATH.")
    
    def do_fbuildrunner(self,arg):
        """run build runner"""
        try:
            result=subprocess.run("flutter pub run build_runner build --delete-conflicting-outputs",shell=True, capture_output=True, text=True)
            self.poutput(cyan+result.stdout+remaining_color)
        except subprocess.CalledProcessError as e:
            self.poutput(f"Error: {e}")
        except FileNotFoundError:
            self.poutput("Flutter not found. Make sure Flutter is installed and in your PATH.")
    def do_firebase_hosting(self,arg):
        """ host flutter web"""
        try:
            result=subprocess.run("npm install -g firebase-tools",shell=True,capture_output=True, text=True)
            self.poutput(result.stdout)
            response=subprocess.run("firebase experiments:enable webframeworks",shell=True,capture_output=True, text=True)
            self.poutput(response.stdout)
            result1=subprocess.run("firebase init hosting",shell=True,capture_output=True, text=True)
            self.poutput(result1.stdout)
            result2=subprocess.run(" firebase deploy",shell=True,capture_output=True, text=True)
            self.poutput(result2.stdout)
        except subprocess.CalledProcessError as e:
            self.poutput(f"Error: {e}")
        except FileNotFoundError:
            self.poutput("Flutter not found. Make sure Flutter is installed and in your PATH.")

    def do_fshot(self,arg):
        """screenshot flutter apps"""
        try:
            result=subprocess.run("flutter screenshot",shell=True,capture_output=True, text=True)
            self.poutput(cyan+result.stdout+remaining_color)
        except subprocess.CalledProcessError as e:
            self.poutput(f"Error: {e}")
        except FileNotFoundError:
            self.poutput("Flutter not found. Make sure Flutter is installed and in your PATH.")

    def do_gclone(self,arg):
        """clone github app"""
        try:
            repoName=input("Enter your repository name: ")
            result=subprocess.run("git clone " +repoName,shell=True,capture_output=True, text=True)
            self.poutput(cyan+"Sucssfully cloned Repository"+remaining_color)
        except subprocess.CalledProcessError as e:
            self.poutput(f"Error: {e}")
        except FileNotFoundError:
            self.poutput("Flutter not found. Make sure Flutter is installed and in your PATH.")
    def do_ginit(self,arg):
        """Initialize github repo"""
        try:
            
            result=subprocess.run("git init ",shell=True,capture_output=True, text=True)
            self.poutput(cyan+result.stdout+remaining_color)
        except subprocess.CalledProcessError as e:
            self.poutput(f"Error: {e}")
        except FileNotFoundError:
            self.poutput("Flutter not found. Make sure Flutter is installed and in your PATH.")
    def do_gcommit(self,arg):
        """commit  message"""
        try:
            commitmessage=input("Enter commit message: ")
            result=subprocess.run("git commit -m " +commitmessage,shell=True, capture_output=True, text=True)
            self.poutput(cyan+result.stdout+remaining_color)
        except subprocess.CalledProcessError as e:
            self.poutput(f"Error: {e}")
        except FileNotFoundError:
            self.poutput("Flutter not found. Make sure Flutter is installed and in your PATH.")
    def do_gadd_all(self,arg):
        """ stage all changes """
        try:
            result=subprocess.run("git add . ",shell=True,capture_output=True, text=True)
            self.poutput(cyan+result.stdout+remaining_color)
        except subprocess.CalledProcessError as e:
            self.poutput(f"Error: {e}")
        except FileNotFoundError:
            self.poutput("Flutter not found. Make sure Flutter is installed and in your PATH.")

    def do_gpush(self,arg):
        """push changes to remote  """
        try:
            
            result=subprocess.run("git push ",shell=True,capture_output=True, text=True)
            self.poutput(cyan+result.stdout+remaining_color)
        except subprocess.CalledProcessError as e:
            self.poutput(f"Error: {e}")
        except FileNotFoundError:
            self.poutput("Flutter not found. Make sure Flutter is installed and in your PATH.")
    def do_gcreate_branch(self,arg):
        """create branch  """
        try:
            repoName=input("Enter your branch name: ")
            result=subprocess.run("git chekout -b "+repoName,shell=True,capture_output=True, text=True)
            self.poutput(cyan+result.stdout+remaining_color)
        except subprocess.CalledProcessError as e:
            self.poutput(f"Error: {e}")
        except FileNotFoundError:
            self.poutput("Flutter not found. Make sure Flutter is installed and in your PATH.")
    def do_gcheckout_branch(self,arg):
        """checkout branch  """
        try:
            repoName=input("Enter  branch name: ")
            result=subprocess.run("git checkout "+repoName,shell=True,capture_output=True, text=True)
            self.poutput(cyan+result.stdout+remaining_color)
        except subprocess.CalledProcessError as e:
            self.poutput(f"Error: {e}")
        except FileNotFoundError:
            self.poutput("Flutter not found. Make sure Flutter is installed and in your PATH.")
    def do_gstatus_check(self,arg):
        """check status  """
        try:
            
            result=subprocess.run("git status ",shell=True,  text=True,capture_output=True)
            self.poutput(cyan+result.stdout+remaining_color)
        except subprocess.CalledProcessError as e:
            self.poutput(f"Error: {e}")
        except FileNotFoundError:
            self.poutput("Flutter not found. Make sure Flutter is installed and in your PATH.")
    def do_glist_branch(self,arg):
        """list branch  """
        try:
            
            result=subprocess.run("git branch ",shell=True, text=True,capture_output=True)
            self.poutput(cyan+ result.stdout+remaining_color)
        except subprocess.CalledProcessError as e:
            self.poutput(f"Error: {e}")
        except FileNotFoundError:
            self.poutput("Flutter not found. Make sure Flutter is installed and in your PATH.")
    
    def do_glog(self,arg):
        """log history  """
        try:
            
            result=subprocess.run("git log ",shell=True, text=True,capture_output=True)
            self.poutput(cyan+result.stdout+remaining_color)
        except subprocess.CalledProcessError as e:
            self.poutput(f"Error: {e}")
        except FileNotFoundError:
            self.poutput("Flutter not found. Make sure Flutter is installed and in your PATH.")



    def do_generate_test_file(self, arg):
        """generates flutter test file"""
        repo_name = input('Enter repository name: ')
        viewmodel_name = input('Enter viewmodel name: ')
        content = f'''
@GenerateMocks([{repo_name}, NavigationService])
void main() {{
  TestWidgetsFlutterBinding.ensureInitialized();
  late {viewmodel_name} viewModel;
  late {repo_name} mock{repo_name};

  setUp(() => {{
        registerStackedMockServices(),
        mock{repo_name} = Mock{repo_name}(),
        removeRegistrationIfExists<{repo_name}>(),
        locator.registerSingleton<{repo_name}>(mock{repo_name}),
        viewModel = {viewmodel_name}(),
      }});
}}
'''

        with open(f'{viewmodel_name.lower()}_test.dart', 'w') as file:
            file.write(content)
        print(cyan+'test file created successfully.'+remaining_color)
    
    

    def do_create_folder_structure(self, args):
        """Generates folder structure"""
        folder_name = input("Enter folder name: ")
        module_name = input("Enter module name: ")
       
        os.makedirs(folder_name, exist_ok=True)
        
       
        subdirectories = ['models', 'services', 'repository', 'views']
        for subdir in subdirectories:
            os.makedirs(os.path.join(folder_name, subdir), exist_ok=True)
        
       
        services_file_content = f'''

        '''
        repository_file_content = f"// {folder_name}_repository.dart\n"
        
        with open(os.path.join(folder_name, 'services', f'{folder_name}_services.dart'), 'w') as services_file:
            services_file.write(services_file_content)
        
        with open(os.path.join(folder_name, 'repository', f'{folder_name}_repository.dart'), 'w') as repository_file:
            repository_file.write(repository_file_content)
        
        
        views_dir = os.path.join(folder_name, 'views', module_name)
        os.makedirs(os.path.join(views_dir, 'viewmodel'), exist_ok=True)
        parts = module_name.split("_")
        formatted_name = ''.join([part.capitalize() for part in parts])

        viewmodel_file_content = f'''
class {formatted_name}Viewmodel extends BaseAppViewModel {{
  
}}
'''
        view_file_content = f'''
import 'package:base/base.dart';
import 'package:flutter/material.dart';

class {formatted_name}View extends BaseStackedView<{formatted_name}Viewmodel> {{
  const {formatted_name}({{
    super.key,
  }});

  @override
  Widget builder(
    BuildContext context,
    {formatted_name}Viewmodel viewModel,
    Widget? child,
  ) {{
    return Scaffold();
  }}

  @override
  {formatted_name}Viewmodel viewModelBuilder(context) => {formatted_name}Viewmodel();
}}
'''
        
        with open(os.path.join(views_dir, 'viewmodel', f'{module_name}_viewmodel.dart'), 'w') as viewmodel_file:
            viewmodel_file.write(viewmodel_file_content)
        
        with open(os.path.join(views_dir, f'{module_name}_view.dart'), 'w') as view_file:
            view_file.write(view_file_content)
        print(cyan+"Folder structure created successfully."+remaining_color)
    
    def do_help(self,args):

        """Command list"""
        helpFlutterCommands = {'fcreate:':" Creates Flutter project",
                        'fanalyze:':" Analyzes the project’s Dart source code.",
                        'ftest:':" Analyzes the projects Dart source code.",
                        'ftestcov:':" Generate and visualize test coverage for your entire app",
                        'frun:':" Run Project",
                        'fver:':" Check Flutter Version",
                        'fpget:':" Get all packages",
                        'fclean:':" Delete the build/ and .dart_tool/ directories.",
                        'fbapk:': " Build Apk",
                        'fbios:': " Build ios",
                        'fgenkey:': " Generate keystore  key",
                        'fbuildrunner:':" Run build runner",
                        'firebase_hosting:':" Host flutter web",
                        'fshot:':" Screenshot flutter apps"}
        i=1
        for key in helpFlutterCommands:
            print(f"{i}."+magenta+key+cyan+helpFlutterCommands[key]+remaining_color)
            i=i+1
        # Printing lines indepenndently and through for loop taking same no of lines so printed manually 
        print()
        print(blue+"***********************Github Related Commands******************************"+remaining_color)
        print("15."+magenta+ "gclone:"+cyan+ " Clone github repo"+remaining_color)
        print("16."+magenta+ "ginit:"+cyan+ " Initialize git"+remaining_color)
        print("17."+magenta+ "gcommit:"+cyan+ " Commit"+remaining_color)
        print("18."+magenta+ "gstage_all:"+cyan+ " Adds a change in the working directory to the staging area"+remaining_color)
        print("19."+magenta+ "gpush:"+cyan+ " Push Changes"+remaining_color)
        print("20."+magenta+ "gcreate_branch:"+cyan+ " Create Branch"+remaining_color)
        print("21."+magenta+ "gcheckout_branch:"+cyan+ " Checkout branch"+remaining_color)
        print("22."+magenta+ "gstatus_check:"+cyan+ " Check Status"+remaining_color)
        print("23."+magenta+ "glist_branch:"+cyan+ " List all branches"+remaining_color)
        print("24."+magenta+ "glog:"+cyan+ " git log"+remaining_color)

        print()
        print(blue+"***********************Folder and file Related Commands******************************"+remaining_color)
        print("25."+magenta+ "generate_test_file:"+cyan+ " Generates Flutter Test File with basic and repititive code"+remaining_color)
        print("26."+magenta+ "create_folder_structure:"+cyan+ " Create Folder structure for flutter app."+remaining_color)
        print("27."+magenta+ "exit:"+cyan+ " exit flutomate"+remaining_color)
        

    def do_exit(self, arg):
        """Exit the Flutomate CLI"""
        self.poutput("Exiting the Flutomate CLI.")
        return True

if __name__ == '__main__':
    art = r'''
,                                                               ,
 \'.                                                           .'/
  ),\                                                         /,( 
 /__\'.                                                     .'/__\
 \  `'.'-.__                                           __.-'.'`  /
  `)   `'-. \                                         / .-'`   ('
  /   _.--'\ '.          ,               ,          .' /'--._   \
  |-'`      '. '-.__    / \             / \    __.-' .'      `'-|
  \         _.`'-.,_'-.|/\ \    _,_    / /\|.-'_,.-'`._         /
   `\    .-'       /'-.|| \ |.-"   "-.| / ||.-'\       '-.    /`
     )-'`        .'   :||  / -.\\ //.- \  ||:   '.        `'-(
    /          .'    / \\_ |  /o`^'o\  | _// \    '.          \
    \       .-'    .'   `--|  `"/ \"`  |--`   '.    '-.       /
     `)  _.'     .'    .--.; |\__"__/| ;.--.    '.     '._  ('
     /_.'     .-'  _.-'     \\ \/^\/ //     `-._  '-.     '._\
     \     .'`_.--'          \\     //          `--._`'.     /
      '-._' /`            _   \\-.-//   _            `\ '_.-'
          `<     _,..--''`|    \`"`/    |`''--..,_     >`
           _\  ``--..__   \     `'`     /   __..--``  /_
          /  '-.__     ``'-;    / \    ;-'``     __.-'  \
         |    _   ``''--..  \'-' | '-'/  ..--''``   _    |
         \     '-.       /   |/--|--\|   \       .-'     /
          '-._    '-._  /    |---|---|    \  _.-'    _.-'
              `'-._   '/ / / /---|---\ \ \ \'   _.-'`
                   '-./ / / / \`---`/ \ \ \ \.-'
                       `)` `  /'---'\  ` `(`
               Himal  /`     |       |     `\
                     /  /  | |       | |  \  \
                 .--'  /   | '.     .' |   \  '--.
                /_____/|  / \._\   /_./ \  |\_____\
               (/      (/'     \) (/     `\)      \)
'''

    # ANSI escape code for green color
    art_color = '\033[91m'
    remaining_color = '\033[92m'
    print(art_color+art+remaining_color)
    print("                       Welcome to Flutomate")
    app = FlutomateCommands()
    app.cmdloop()