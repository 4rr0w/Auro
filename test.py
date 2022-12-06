from bs4 import BeautifulSoup
import pandas as pd

class Order:
    def createorder():
        pass
    
    def deleteorder():
        pass
    
def main():
    #I am using testorders.xml = 200 entries from oridinal file for debugging and testing
    with open('testorders.xml', 'r') as f:
        data = f.read() 
        
    soup = BeautifulSoup(data, 'xml') 
    
    add_df = pd.DataFrame(columns=['book', 'operation', 'orderId', 'price', 'volume'])
    del_df = pd.DataFrame(columns=['book', 'orderId'])
    
    
    addorders = soup.find_all('AddOrder')
    deleteorders = soup.find_all('DeleteOrder')
    
    for index, add_order in enumerate(addorders):
        print(add_order.attrs)
        book = add_order.attrs['book']
        operation = add_order.attrs['operation']
        orderId = add_order.attrs['orderId']
        price = add_order.attrs['price']
        volume = add_order.attrs['volume']
        
        row = {
            'book': book, 
            'operation' : operation, 
            'orderId': orderId, 
            'price': price, 
            'volume': volume,            
        }
        
        add_df = add_df.append(row, ignore_index=True)
        
    
    for index, del_order in enumerate(deleteorders):
        book = del_order.attrs['book']
        orderId = del_order.attrs['orderId']
        row = {
            'book': book, 
            'orderId': orderId,     
        }
        
        del_df = del_df.append(row, ignore_index=True)
    
    pd.merge(add_df, del_df, indicator=True, how='outer').query('_merge=="left_only"').drop('_merge', axis=1)
    
    print(add_df)

if __name__=="__main__":
    main()