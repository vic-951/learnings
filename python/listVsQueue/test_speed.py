from collections import deque
from datetime import datetime
import sys

def add_or_remove_in_array(list):
  if(len(list) < 1): return -1
  storage = []

  for request in list:
    req, value = split_request(request)

    if req == "hinzufügen":
      storage.append(value)
    elif req == "entfernen":
      if value in storage:
        storage.remove(value)

  return storage

def add_or_remove_in_queue(list):
  if(len(list) < 1): return -1
  queue = deque()

  for request in list:
    req, value = split_request(request)

    if req == "hinzufügen":
      queue.append(value)
    elif req == "entfernen":
      if value in queue:
        queue.remove(value)
  
  return queue

def add_or_remove_in_array_fifo(list):
  if(len(list)<1): return -1
  storage = []

  for request in list:
    req, value = split_request(request)
    if req == "hinzufügen":
      storage.append(value)
    elif req == "entfernen":
      storage.pop(0)
  
  return storage

def add_or_remove_in_queue_fifo(list):
  if(len(list)<1): return -1
  queue = deque()

  for request in list:
    req, value = split_request(request)
    if req == "hinzufügen":
      queue.append(value)
    elif req == "entfernen":
      queue.popleft()

  return queue

def split_request(line: str):
  parts = line.split()
  request = parts[0].lower()
  value = parts[1]

  return request,value

def get_duration(start,end):
  duration = end - start
  duration = duration.total_seconds()
  

  hours = int(duration // 3600)
  duration %= 3600
  minutes = int(duration // 60)
  duration %= 60
  seconds = int(duration % 60)
  milliseconds = int((duration % 1) * 1000)

  response = []
  if hours:
    response.append(f"{hours} h")
  if minutes:
    response.append(f"{minutes} min.")
  if seconds:
    response.append(f"{seconds} s")
  if milliseconds:
    response.append(f"{milliseconds} ms")

  return ", ".join(response)

def get_size_in_byte(obj, seen=None):
  import sys
  from queue import Queue
  if seen is None:
    seen = set()

  obj_id = id(obj)
  if obj_id in seen:
    return 0
  seen.add(obj_id)

  size = sys.getsizeof(obj)

  if isinstance(obj, dict):
    for k, v in obj.items():
      size += get_size_in_byte(k, seen)
      size += get_size_in_byte(v, seen)

  elif isinstance(obj, (list, tuple, set, frozenset, deque)):
    for item in obj:
      size += get_size_in_byte(item, seen)

  elif isinstance(obj, Queue):
    size += get_size_in_byte(list(obj.queue), seen)

  # neu:
  elif hasattr(obj, "__dict__"):
    size += get_size_in_byte(vars(obj), seen)

  elif hasattr(obj, "__slots__"):
    for slot in obj.__slots__:
      if hasattr(obj, slot):
        size += get_size_in_byte(getattr(obj, slot), seen)

  return size

def render_bytes(size: int) -> str:
  KB = 1024
  MB = KB * 1024
  GB = MB * 1024

  gigibyte = int(size // GB)
  size %= GB
  mebibyte = int(size // MB)
  size %= MB
  kibibyte = int(size // KB)
  size %= KB
  byte = size % KB

  response = []
  if gigibyte:
    response.append(f"{gigibyte} GiB")
  if mebibyte:
    response.append(f"{mebibyte} MiB")
  if kibibyte:
    response.append(f"{kibibyte} KiB")
  if byte:
    response.append(f"{byte} Byte")
  
  return ", ".join(response)

if __name__ == "__main__":
  request_list = []
  with open("exampleList.txt", "r", encoding="utf-8") as f:
    for row in f:
      request_list.append(row)

  print("Teste Anfragen in einem Array")
  start = datetime.now()
  tmp_list = add_or_remove_in_array(request_list)
  print("Benötigte Zeit:", get_duration(start, datetime.now()))
  print("Größe in Bytes:", render_bytes(get_size_in_byte(tmp_list)))
  print()

  print("Teste Anfragen in einer Queue")
  start = datetime.now()
  tmp_list = add_or_remove_in_queue(request_list)
  print("Benötigte Zeit:", get_duration(start, datetime.now()))
  print("Größe in Bytes:", render_bytes(get_size_in_byte(tmp_list)))
  print()

  print("Teste Anfragen in einem Array nach FIFO")
  start = datetime.now()
  tmp_list = add_or_remove_in_array_fifo(request_list)
  print("Benötigte Zeit:", get_duration(start, datetime.now()))
  print("Größe in Bytes:", render_bytes(get_size_in_byte(tmp_list)))
  print()

  print("Teste Anfragen in einer Queue nach FIFO")
  start = datetime.now()
  tmp_list = add_or_remove_in_queue_fifo(request_list)
  print("Benötigte Zeit:", get_duration(start, datetime.now()))
  print("Größe in Bytes:", render_bytes(get_size_in_byte(tmp_list)))