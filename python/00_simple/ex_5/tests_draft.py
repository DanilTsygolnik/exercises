import unittest
import random
import draft

class TestEx_5(unittest.TestCase):

    def test_SynchronizingTables(self):

        def get_values(N):
            s_sal = []
            cnt = 0
            while cnt < N:
                s_sal += [10000 * random.randint(1, 10)]
                cnt += 1
            s_sal.sort()
        
            s_ids = []
            emp = {}
            cnt = 0
            while cnt < N:
                while True:
                    curr_id = random.randint(1, 10000)
                    if curr_id in emp:
                        continue
                    else:
                        s_ids += [curr_id]
                        emp[curr_id] = curr_id
                        break
                cnt += 1
            s_ids.sort()
        
            # pairs
            cnt = 0
            while cnt < N:
                emp[s_ids[cnt]] = s_sal[cnt]
                cnt += 1
        
            ids = list(s_ids)
            random.shuffle(ids)
        
            sal = []
            for id in ids:
                sal += [emp[id]]
        
            sal_mess = list(sal)
            random.shuffle(sal_mess)
            
            values = {}
            values['ids'] = ids
            values['sal'] = sal 
            values['sal mess'] = sal_mess
            return values
        
        self.assertEqual(draft.SynchronizingTables(3, [50, 1, 1024], [20000, 100000, 90000]), [90000, 20000, 100000])

        N = int(random.randint(1, 50))
        val = get_values(N)
        self.assertEqual(draft.SynchronizingTables(N, val['ids'], val['sal mess']), val['sal'])

if __name__ == "__main__":
    unittest.main()


#N = int(random.randint(50))
#val = get_values(N)
#print("ids")
#print(val['ids'])
#print("sal carrect")
#print(val['sal'])
#print("sal messed")
#print(val['sal mess'])
#print("sal fixed")
#print(draft.SynchronizingTables(N, val['ids'], val['sal mess']))
