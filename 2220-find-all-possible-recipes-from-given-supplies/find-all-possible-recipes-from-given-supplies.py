class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        cando=[i for i in supplies]

        recipe_map={recipes[i]:i for i in range(len(recipes))}

        visit=set()



        def dfs(r):
            #print(r)
            if r in visit:
                return False
            
            if r in cando:
                return True
            
            if r not in recipe_map:
                return False
        
            visit.add(r)

            for ing in ingredients[recipe_map[r]]:
                if not dfs(ing):
                    return False
            

            visit.remove(r)
            cando.append(r)
            return True
        

        ans=[]

        for i in recipes:
            if dfs(i):
                ans.append(i)
                
        return ans
        


        