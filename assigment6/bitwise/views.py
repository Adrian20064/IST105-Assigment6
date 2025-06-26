from django.shortcuts import render
from models import NumberForm
from pymongo import MongoClient
# Create your views here.

Mongo_URI = "mongodb://admin:password123@18.212.35.5:27017/assignment6"
client = MongoClient(Mongo_URI)

def process_number(request):
    result = None
    
    if request.method == 'POST':
        form = NumberForm(request.POST)
        if form.is_valid():
            values = [form.cleaned_data[f] for f in  ['a', 'b', 'c', 'd', 'e']]
            negatives = [v for v in values if v < 0]
            avg = sum(values)/5
            positive_count = sum(1 for v in values if v >= 0)
            bitwise_even = [(v,v&1==0)for v in values]
            filtered_sortes = sorted([v for v in values if v > 10])
            
            result = {
                'original': values,
                'negatives': negatives,
                'average': avg,
                'average_minumn': avg > 50,
                'positive_count': positive_count,
                'bitwise_even': bitwise_even,
                'filtered_sorted': filtered_sortes
            }
            
            try:
                client = MongoClient(Mongo_URI)
                db = client['assigment6']
                db.entries.insert_one({
                    'input':values,
                    'result':result
                })
            except Exception as e:
                print(f"Error connecting to MongoDB: {e}")
                result['error'] = "Failed to save data to MongoDB."
        else:
            form = NumberForm()
            
        return render(request,'bitwise/form.html', {'form': form, 'result': result})