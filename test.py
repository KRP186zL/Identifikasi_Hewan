import time

def loading_animation(duration):
    start_time = time.time()
    while time.time() - start_time < duration:
        for i in range(4):
            print("Loading" + "." * i)
            time.sleep(0.5)
            print("\033[F\033[K", end="")  # Menghapus baris sebelumnya
        
loading_animation(3)
