# Task 
### Write a function to calculate the delivery cost.
The cost is calculated based on:

**distance to the destination**:

- more than 30 km: +300 rubles to the delivery cost;
- up to 30 km: +200 rubles to the delivery cost;
- up to 10 km: +100 rubles to the delivery cost;
- up to 2 km: +50 rubles to the delivery cost;

**dimensions of the cargo**:

- large dimensions: +200 rubles to the delivery cost;
- small dimensions: +100 rubles to the delivery cost;
  
**fragility of the cargo**. 
- If the cargo is fragile, add +300 rubles to the delivery cost. Fragile cargo cannot be transported for distances greater than 30 km;

**load of the delivery service.** 
- The cost is multiplied by the delivery load coefficient:
  - very high load — 1.6;
  - high load — 1.4;
  - increased load — 1.2;
- In all other cases, the coefficient is 1.

**minimal cost of delivery**
- The minimum delivery cost is 400 rubles. If the delivery cost is less than the minimum, the minimum amount is output.


The function receives the distance to the destination, dimensions, information about fragility, and the current load of the service as inputs. The output is the delivery cost.

# Install
### Environment setup, git workflow
Local Machine Installation & Configuration for a Python Testing Automation project
- https://gist.github.com/KirillY/6a39310b1fea1a8cc7d0d81632426c99

### Install packages and venv
```shell
cd /path/to/project/root
pdm install
```

# Run tests
```shell
cd /path/to/project/root
```
### Run all tests
```shell
pdm run python -m pytest
```

### Run selected test by name
```shell
pdm run python -m pytest -k test_name
```


