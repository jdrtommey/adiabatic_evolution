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
        self.state_list= self.State_init(self.Diagonaliser.h0)

    def mainloop(self):
            """
            performs each iteration, calculates what the next sigma should be, calls the methods
            to pair the eigenvectors to the adiabatic ones.
            """
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
