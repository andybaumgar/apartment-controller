from apartment_controller import ac_controller, light_controller
import concurrent.futures


def run_all_loops():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.submit(light_controller.run)
        executor.submit(ac_controller.run)


if __name__ == "__main__":
    run_all_loops()
