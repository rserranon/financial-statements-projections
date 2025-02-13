import modelx as mx

class ModelSingleton:
    """Singleton class to hold the model instance"""
    
    _instance = None  # Static variable to store the instance

    @staticmethod
    def get_instance():
        """Static method to get the instance of the model."""
        if ModelSingleton._instance is None:
            ModelSingleton._instance = mx.new_model(name='Financial_Statements_Model')
        return ModelSingleton._instance
