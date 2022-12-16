class BaseCharacterConverter():
    def test_converter(self):
        for (inputs, outputs) in self.inputs_and_outputs:
            with self.subTest(inputs = inputs):
                self.assertEqual(outputs, self.converter()(inputs))