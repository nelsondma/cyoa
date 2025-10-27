function LoadingStatus({theme}) {
    return <div className="loading-container">
            
            <h2>Generating your {theme} Story...</h2>
            <p>This may take a few minutes...</p>
            
            <div className="loading-animation">
                <div className="spinner"></div>
            </div>
            
            <p className="loading-info">
                Please wait while we generate your story...
            </p>
    </div>
    
}

export default LoadingStatus;
    