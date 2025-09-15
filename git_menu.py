import subprocess
import platform

def runReturnCommand ( command, operationName ) -> bool :
    result = subprocess.run ( command, capture_output = True, text = True )
    
    if result.returncode == 0 :
        print ( f"Successfully { operationName }! " )
        return True
    else :
        print ( f"Error { operationName } Failed" )
        return False

def gc ( mensagem  ) -> bool :
    returnGitCommitValue = True
    
    print ( )
    returnGitCommitValue = returnGitCommitValue and runReturnCommand ( [ "git", "add", "." ], "git add process" )
    returnGitCommitValue = returnGitCommitValue and runReturnCommand ( [ "git", "commit", "-m", mensagem ], "git commit process" )
    
    return returnGitCommitValue
    
def gpl ( ) -> bool :
    print ( )

    return runReturnCommand ( [ "git", "pull" ], "git pull process" )

def gps ( ) -> bool :
    print ( )

    return runReturnCommand ( [ "git", "push" ], "git push process" )
    
def clearSystem ( ) :
    if platform.system ( ) == "Windows" :
        subprocess.run ( [ "cls" ], shell = True )

    else :
        subprocess.run ( [ "clear" ] )

def menu ( ) :
    print ( "======= Welcome To Git Menu =======" )
    print ( "0 - Exit" )
    print ( "1 - Commit" )
    print ( "2 - Push" )
    print ( "3 - Pull" )

def main ( ) -> int :
    option = - 1
    
    while option != 0 :
        clearSystem ( )
        menu ( )
        
        option = int ( input ( "\nChoose One Option : " ) )
        
        if option < 0 :
            while option < 0 :
                clearSystem ( )
                menu ( )
                print ( "\nChoose The Valid Value ! Option >= 0" )
                option = int ( input ( "Choose A Valid Value : " ) )
    
        if option == 0 :
            print ( "Exit Program ..." )
            return 0
        
        elif option == 1:
            mensagem = input ( "\nWrite A Message Commit : " )
            returnGitCommitValue = gc ( mensagem )
            
            if returnGitCommitValue == True :
                print ( "Successfully Commit !\n" );
            else :
                print ( "Failed Commit\n" )
            
        elif option == 2 :
            returnGitPushValue = gps ( )
            
            if returnGitPushValue == True :
                print ( "Successfully Push !\n" );
            else :
                print ( "Failed Push\n" )
            
        else :
            returnGitPullValue = gpl ( )
            
            if returnGitPullValue == True :
                print ( "Successfully Pull !\n" );
            else :
                print ( "Failed Pull\n" )
            
        print ( "Press Enter To Continue ..." )
        input ( )

    return 1
    
if __name__ == "__main__" :
    returnValueMain = main ( )
    print ( f"Program Return : { returnValueMain }" )