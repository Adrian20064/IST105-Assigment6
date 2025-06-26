from django.shortcuts import render
from bitwise.forms import NumberForm
from pymongo import MongoClient

# Conexión a MongoDB
MONGO_URI = "mongodb://admin:password123@18.212.35.5:27017/assignment6"
#FEEATURE1
def process_number(request):
    result = None

    if request.method == 'POST':
        form = NumberForm(request.POST)
        if form.is_valid():
            values = [form.cleaned_data[f] for f in ['a', 'b', 'c', 'd', 'e']]
            sum_values = sum(values)
            avg = sum_values / len(values)
            max_value = max(values)
            min_value = min(values)
            product = 1
            for v in values:
                product *= v

            result = {
                'original': values,
                'sum': sum_values,
                'average': avg,
                'maximum': max_value,
                'minimum': min_value,
                'product': product,
                'negatives': [v for v in values if v < 0],
                'average_minimum': avg > 50,
                'positive_count': sum(1 for v in values if v > 0),
                'bitwise_even': [(v, v & 1 == 0) for v in values],
                'filtered_sorted': sorted([v for v in values if v > 10])
            }
                        
            try:
                client = MongoClient(MONGO_URI)
                db = client['assignment6']  
                db.entries.insert_one({
                    'input': values,
                    'result': result
                })
            except Exception as e:
                print(f"Error connecting to MongoDB: {e}")
                result['error'] = "Failed to save data to MongoDB."
    else:
        form = NumberForm()

    return render(request, 'bitwise/form.html', {'form': form, 'result': result})
