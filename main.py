from handlers.simulation_handler import SimulationHandler


def main() -> None:
    """Main function to start the simulation."""
    handler = SimulationHandler()
    handler.run()


if __name__ == "__main__":
    main()
