#import myModule
import myModule as mmd
from myModule import testMe, importedVar

print 'hello form test'
myItems = ['pen', 'smartphone', 'laptop']

indexTest = mmd.index(myItems, 'laptop')
print indexTest
print testMe + ':' + importedVar
myLogin = mmd.login('Nikos', '23a56#')
print myLogin
numbers = mmd.randomFunction(1, 20)
print numbers
checking = mmd.checkIfString(testMe)
print checking
