#Suppose you have N men and N women, and each person has ranked their prospective opposite-sex partners in order of preference.
#Write an algorithm that pairs the men and women together in such a way that no two people of opposite sex would both rather be with each other than with their current partners.

#This is a well known algorithm, I did not figure it out myself, it should work in O(n^2) time

guy_preferences = {

'andrew': ['caroline', 'abigail', 'betty'],
'bill': ['caroline', 'betty', 'abigail'],
'chester': ['betty', 'caroline', 'abigail'],
}

gal_preferences = {

'abigail': ['andrew', 'bill', 'chester'],
'betty': ['bill', 'andrew', 'chester'],
'caroline': ['bill', 'chester', 'andrew']
}  

def assign(guy_matrix, gal_matrix):


    acceptor_matrix = {}
    proposer_matrix = {}

    #for the first pass through the matrix, each man will propose to his top choice gal. If a gal is proposed to, she will accept her highest ranked suitor as a fiance with the option to swap him out later for a higher rank

    for key in guy_matrix:
        top_choice_gal = guy_matrix[key][0]
        if (top_choice_gal not in acceptor_matrix):
            acceptor_matrix[top_choice_gal] = key
            proposer_matrix[key] = top_choice_gal
        else:
            temp_list = gal_matrix[top_choice_gal]
            if (temp_list.index(key) < temp_list.index(acceptor_matrix[top_choice_gal])):

                #these 2 lines update the proposer matrix if a guy had been selected earlier but then unselected in this round
                booted_guy = acceptor_matrix[top_choice_gal]
                del proposer_matrix[booted_guy]

                proposer_matrix.update({key:top_choice_gal})
                acceptor_matrix.update({top_choice_gal:key})
            
 

    #following passes through the matrix will follow this logic
    #Guys who have not yet proposed and received a conditional yes will propose to their next choice. The gal will accept if the she is not currently engaged (first loop only) or if she prefers the man over her current fiance
    i = 1
    while (i < len(guy_matrix)):
        for key in guy_matrix:
            next_choice_gal = guy_matrix[key][i]
            if (key not in proposer_matrix):
                if (next_choice_gal not in acceptor_matrix):
                    proposer_matrix[key] = next_choice_gal
                    acceptor_matrix[next_choice_gal] = key
                #checks to see if gal prefers guy over current fiance
                else:
                    temp_list = gal_matrix[next_choice_gal]
                    if (temp_list.index(key) < temp_list.index(acceptor_matrix[next_choice_gal])):
                        proposer_matrix.update({key:next_choice_gal})
                        acceptor_matrix.update({next_choice_gal:key})
        i+=1

    for key in proposer_matrix:
        print("Guy is", key, "and gal is ", proposer_matrix[key])
 
        

assign({

'andrew': ['caroline', 'abigail', 'betty'],
'bill': ['caroline', 'betty', 'abigail'],
'chester': ['betty', 'caroline', 'abigail'],
}
,
{

'abigail': ['andrew', 'bill', 'chester'],
'betty': ['bill', 'andrew', 'chester'],
'caroline': ['bill', 'chester', 'andrew']
}  
)
                    


        




            


