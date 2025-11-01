~ $ aws cloudwatch get-metric-statistics \
>   --namespace AWS/Bedrock \
>   --metric-name InputTokenCount \
>   --dimensions Name=ModelId,Value=amazon.nova-micro-v1:0 \
>   --start-time 2025-10-01T00:00:00Z \
>   --end-time 2025-11-01T00:00:00Z \
>   --period 86400 \
>   --statistics Average Sum SampleCount Minimum Maximum \
>   --region us-east-1
{
    "Label": "InputTokenCount",
    "Datapoints": [
        {
            "Timestamp": "2025-10-29T00:00:00+00:00",
            "SampleCount": 2.0,
            "Average": 1424.0,
            "Sum": 2848.0,
            "Minimum": 1323.0,
            "Maximum": 1525.0,
            "Unit": "Count"
        }
    ]
}
~ $ aws cloudwatch get-metric-statistics \
>   --namespace AWS/Bedrock \
>   --metric-name OutputTokenCount \
>   --dimensions Name=ModelId,Value=amazon.nova-micro-v1:0 \
>   --start-time 2025-10-01T00:00:00Z \
>   --end-time 2025-11-01T00:00:00Z \
>   --period 86400 \
>   --statistics Average Sum SampleCount Minimum Maximum \
>   --region us-east-1
{
    "Label": "OutputTokenCount",
    "Datapoints": [
        {
            "Timestamp": "2025-10-29T00:00:00+00:00",
            "SampleCount": 2.0,
            "Average": 174.0,
            "Sum": 348.0,
            "Minimum": 164.0,
            "Maximum": 184.0,
            "Unit": "Count"
        }
    ]
}
~ $ 
