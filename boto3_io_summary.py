import boto3
from datetime import datetime

# Initialize CloudWatch client
cloudwatch = boto3.client('cloudwatch', region_name='us-east-1')  # Change region as needed

# Define parameters
model_id = 'amazon.nova-micro-v1:0'
start_time = datetime(2025, 10, 1, 0, 0, 0)
end_time = datetime(2025, 11, 1, 0, 0, 0)

# Get Input Token metrics
input_response = cloudwatch.get_metric_statistics(
    Namespace='AWS/Bedrock',
    MetricName='InputTokenCount',
    Dimensions=[
        {
            'Name': 'ModelId',
            'Value': model_id
        }
    ],
    StartTime=start_time,
    EndTime=end_time,
    Period=2678400,  # 31 days in seconds (entire October)
    Statistics=['Average', 'Sum', 'SampleCount', 'Minimum', 'Maximum']
)

# Get Output Token metrics
output_response = cloudwatch.get_metric_statistics(
    Namespace='AWS/Bedrock',
    MetricName='OutputTokenCount',
    Dimensions=[
        {
            'Name': 'ModelId',
            'Value': model_id
        }
    ],
    StartTime=start_time,
    EndTime=end_time,
    Period=2678400,  # 31 days in seconds
    Statistics=['Average', 'Sum', 'SampleCount', 'Minimum', 'Maximum']
)

# Display results
print("=" * 60)
print(f"Token Usage Statistics for {model_id}")
print(f"Period: October 2025")
print("=" * 60)

if input_response['Datapoints']:
    input_data = input_response['Datapoints'][0]
    print("\n📥 INPUT TOKENS:")
    print(f"  Average per invocation: {input_data.get('Average', 0):.2f}")
    print(f"  Total tokens: {input_data.get('Sum', 0):,.0f}")
    print(f"  Total invocations: {input_data.get('SampleCount', 0):,.0f}")
    print(f"  Min tokens: {input_data.get('Minimum', 0):.0f}")
    print(f"  Max tokens: {input_data.get('Maximum', 0):.0f}")
else:
    print("\n📥 INPUT TOKENS: No data available")

if output_response['Datapoints']:
    output_data = output_response['Datapoints'][0]
    print("\n📤 OUTPUT TOKENS:")
    print(f"  Average per invocation: {output_data.get('Average', 0):.2f}")
    print(f"  Total tokens: {output_data.get('Sum', 0):,.0f}")
    print(f"  Total invocations: {output_data.get('SampleCount', 0):,.0f}")
    print(f"  Min tokens: {output_data.get('Minimum', 0):.0f}")
    print(f"  Max tokens: {output_data.get('Maximum', 0):.0f}")
else:
    print("\n📤 OUTPUT TOKENS: No data available")
