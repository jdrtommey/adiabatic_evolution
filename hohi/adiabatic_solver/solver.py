from tqdm import tqdm

class Solver:
    def __init__(self,State_init,Matcher,Sigma_guesser,Diagonaliser,parameters,sigma_init):
        """
        solver class is a loop which computes eigenvalues and eigenvectors, and calls various plug-in classes
        to perform logic on the output values. Not intended to be called by a person, the userinterface generates this
        class.
        
        Parameters
        ----------

        """
        self.parameters = parameters
        self.sigma_init = sigma_init

        # The plug-in classes which provide the logical operations on the eigenvectors
        self.Matcher = Matcher
        self.Sigma_guesser = Sigma_guesser
        self.Diagonaliser = Diagonaliser
        self.State_init = State_init

    def mainloop(self):
            """
            performs each iteration, calculates what the next sigma should be, calls the methods
            to pair the eigenvectors to the adiabatic ones.
            """
            state_list= self.State_init(self.Diagonaliser.h0)
            sigma = self.sigma_init
            all_failures = []
            for p in tqdm(self.parameters):
                vals,vecs = self.Diagonaliser(p,sigma)                  #compute vals/vecs
                self.state_list,self.fail_list = self.Matcher(self.state_list,vals,vecs,p)    #updates the state_list
                sigma = self.Sigma_guesser(sigma,self.state_list)  #update the sigma
                
                for failed in self.fail_list:
                    all_failures.append([failed,p])
                    
                if len(self.state_list) == 0 :
                    raise RuntimeError("No adiabatic states left to calculate")
            
            return self.state_list,all_failures #at end of cycle return the final list of adiabatic states calculated.
        
        
    def doloop(self):
        """
        take a max value and initial guess, 
        """
        state_list = self.State_init(self.Diagonaliser.h0)
        failed_list = []
        
        while parameter < parameter_maximum:
            vals,vecs = self.Diagonaliser(parameter,sigma)  #compute vals/vecs
            successful_matches,failed_matches = self.Matcher(state_list,vals,vecs,parameter) #pair eigenvals to adiabatic states
            
            for failure in failed_matches:
                failed_list.append([failure,parameter])
            sigma = self.Sigma_guesser(sigma,state_list)               #update the sigma guess
            parameter = self.parameter_updater(state_list,fail_list)   #compute a new paramter value