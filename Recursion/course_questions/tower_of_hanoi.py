def tower_of_hanoi(n, from_rod="A", auxilary_rod="B", to_rod="C"):
    if n == 0:
        return
    tower_of_hanoi(n-1, from_rod, to_rod, auxilary_rod)
    print(f"Move disk {n} from {from_rod} to {to_rod}")
    tower_of_hanoi(n-1, auxilary_rod, from_rod, to_rod)


tower_of_hanoi(3)
