from modified_queue import modified_queue


if __name__ == "__main__":
    # Create a modified queue with id 'queue1' and max size 3
    mq = modified_queue('queue1', max_size=3)
    
    # Enqueue some items
    mq.enqueue(10)
    mq.enqueue(20)
    mq.enqueue(30)
    
    # Try to enqueue another item to test max size exception
    try:
        mq.enqueue(40)
    except Exception as e:
        print(e)  # Output: Queue has reached its maximum size

    # Save the current state of all queues
    modified_queue.save()
    
    # Load the queues from the saved state
    modified_queue.load()
    
    # Access the loaded queue and print its items
    loaded_mq = modified_queue.all_ques['queue1']
    print(loaded_mq.get_items())  # Output: [10, 20, 30]