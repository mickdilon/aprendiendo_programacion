<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="author" content="Miguel Angel Garcia Cambron" />
    <meta name="copyright" content="Propietario del copyright" />   
    <meta name="description" content="Codigo para facilitar el aprendizaje y comprension de funcion secuencial Fibonacci, para mayor informes, contactar al correo siguiente: ingmiguelangelgc@gmail.com"/>

      <title>Secuencia de Fibonacci</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 20px;
        }
        #result {
            margin-top: 20px;
            font-size: 18px;
            color: #333;
        }
    </style>
</head>
<body>
    <h1>Secuencia de Fibonacci</h1>
    <p>Ingresa la cantidad de números que deseas generar:</p>
    <form method="post">
        <input type="number" name="num" min="1" placeholder="Ejemplo: 10" required>
        <button type="submit">Generar</button>
    </form>

    <div id="result">
        <?php
        if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['num'])) {
            $num = intval($_POST['num']); // Obtener el número ingresado por el usuario

            if ($num > 0) {
                // Generar la secuencia de Fibonacci
                function generateFibonacci($n) {
                    $fibonacci = [0, 1];
                    for ($i = 2; $i < $n; $i++) {
                        $fibonacci[] = $fibonacci[$i - 1] + $fibonacci[$i - 2];
                    }
                    return array_slice($fibonacci, 0, $n); // Retornar solo los primeros $n números
                }

                $sequence = generateFibonacci($num);

                // Mostrar la secuencia
                echo "<h2>Resultado:</h2>";
                echo "<p>" . implode(", ", $sequence) . "</p>";
            } else {
                echo "<p style='color: red;'>Por favor, ingresa un número válido mayor que 0.</p>";
            }
        }
        ?>
    </div>
</body>
</html>
